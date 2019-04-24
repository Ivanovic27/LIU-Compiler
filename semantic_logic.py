from preloaded_data import mapping_functions
import copy
from preloaded_data import global_function
from globals import (global_data as gl, memory)
from validations import *
from Function import Function
from Variable import Variable
from GroupItem import GroupItem
from utils import list_params_to_dict
from Operator import Operator

types = {
    "both": gl.add_continuous_quadruples,
    "left": gl.add_left_quadruples
}

def create_variable(variable_name, literal):
    check_variable_type(variable_name, literal)
    variable = gl.get_variable(variable_name)
    if not variable:
        # Add variable if not already declared.
        new_dir = gl.get_last_data()
        gl.add_memory(None)
        new_variable = Variable(variable_name, literal.type, new_dir)
        gl.add_variable(variable_name, new_variable)
        variable = gl.get_variable(variable_name)
    memory.add_assign(literal.virtual_direction, variable.virtual_direction)


def definition_function_parameters(self, ctx, parameters):
    counter = 0
    new_parameters = []
    for param in parameters:
        new_parameters.append(self.parameters(param))
    for param in new_parameters:
        current_position = 0
        finish = False
        while not finish:
            found_item = False
            for (key, attr) in param.items():
                if attr.pos == current_position:
                    attr.global_pos = counter
                    counter += 1
                    current_position += 1
                    found_item = True
                    break
            if not found_item:
                finish = True
    return list_params_to_dict(new_parameters)


def do_function_execution(self, ctx):
    (function_name, grps) = get_execution_data(self, ctx)
    func = gl.functions[function_name]
    memory.add_quadruple(Operator.ERA, func.virtual_directon, None, None)
    (new_function_name, groups) = do_execution(
        self, grps, function_name)
    parameters = gl.functions[function_name].parameters
    for group in groups:
        for key, parameter in parameters.items():
            if parameter.pos == group.pos and parameter.param == group.param:
                memory.add_quadruple(
                    Operator.PARAM, group.virtual_direction, None, parameter.virtual_direction)
    memory.add_quadruple(Operator.GOSUB, func.code_direction, None, None)
    return (new_function_name, func.virtual_directon)

def get_id(ctx):
    id = ctx.Id()
    if id != None:
        rest_id = get_id(ctx.identification2())
        return id.getText() + rest_id
    return ""


def create_function(self, ctx, function_name, parameters, initial_virtual_direction):
    # Ensure the new function is not already defined
    check_defined_function(function_name)
    code_virtual_direction = memory.get_last_code() + 1
    # Add the function to the functions table
    gl.functions[function_name] = Function(
        function_name, None, {}, parameters, False, initial_virtual_direction, code_virtual_direction)
    memory.add_quadruple(Operator.PARAMEND, None, None, None)
    self.function(ctx.function())
    gl.current_scope = global_function
    memory.add_quadruple(Operator.ENDPROC, None, None, None)
    memory.local_segment.clear()


def get_group_variables(self, ctx, current_position=0):
    if ctx.literal() != None:
        item = self.literal(ctx.literal())
        new_item = GroupItem(item.type, current_position,
                             item.virtual_direction)
        rest_items = get_group_variables(
            self, ctx.group3(), current_position + 1)
        return [new_item] + rest_items
    return []


def get_list_variables(self, ctx, current_position=0, last_item = None):
    first_direction = None
    if ctx.literal() != None:
        item = self.literal(ctx.literal())
        value_dir = gl.get_last_data()
        gl.add_memory(None)
        memory.add_assign(item.virtual_direction, value_dir)
        next_dir = gl.get_last_data()
        gl.add_memory(None)
        memory.add_assign(None, next_dir)
        if last_item == None:
            first_direction = value_dir
        else:
            memory.add_quadruple(Operator.MEM, value_dir, None, last_item)
        new_item = GroupItem(item.type, current_position,
                             item.virtual_direction)
        (_, rest_items) = get_list_variables(
            self, ctx.list3(), current_position + 1, next_dir)
        return (first_direction, [new_item] + rest_items)
    return (first_direction, [])


def do_execution(self, groups, function_name):
    parameters = []
    for index, group in enumerate(groups):
        current_parameters = self.group(group)
        current_parameters = current_parameters.variables
        for parameter in current_parameters:
            parameter.param = index
        parameters.extend(current_parameters)
    check_function_exists(parameters, function_name)
    return (function_name, parameters)


def do_default_execution(self, ctx):
    for name, operation in mapping_functions.items():
        if getattr(ctx, name) and getattr(ctx, name)() != None:
            new_ctx = getattr(ctx, name)()
            groups = new_ctx.group()
            if not isinstance(groups, (list)):
                groups = [new_ctx.group()]
            (function_name, parameters) = do_execution(
                self, groups, operation["name"])
            return (function_name, types[operation["type"]](operation["operation"], parameters))


def do_if_execution(self, ctx):
    (_, parameters) = do_execution(
        self, [ctx.group()], "if(param)")
    condition_dir = parameters[0].virtual_direction
    memory.add_gotoFalse(condition_dir)
    gl.add_jump(-1)
    self.function(ctx.function())
    self.else_execution(ctx)


def do_else_execution(self, ctx):
    if ctx.Else() != None:
        else_dir = gl.pending_jumps.pop()
        memory.fill_jump(else_dir, 1)
        memory.add_goto(None)
        gl.add_jump(-1)
        if ctx.function() != None:
            self.function(ctx.function())
        else:
            self.if_execution(ctx)
    end_dir = gl.pending_jumps.pop()
    memory.fill_jump(end_dir)


def do_iterate_execution(self, ctx):
    gl.add_jump()
    (_, parameters) = do_execution(
        self, [ctx.group()], "iteratewhile(param)")
    condition_dir = parameters[0].virtual_direction
    memory.add_gotoFalse(condition_dir)
    gl.add_jump(-1)
    self.function(ctx.function())
    begin_dir = gl.pending_jumps.pop()
    end_dir = gl.pending_jumps.pop()
    memory.add_goto(end_dir)
    memory.fill_jump(begin_dir)


def get_parameters_data(self, ctx, param_position=0):
    parameters = {}
    if ctx.definition() != None:
        (name, type, direction) = self.defintion_parameter(ctx.definition())
        parameters = get_parameters_data(
            self, ctx.parameters2(), param_position + 1)
        parameters[name] = GroupItem(type.type, param_position)
        parameters[name].virtual_direction = direction
    return parameters


def get_execution_data(self, ctx):
    id = ""
    groups = []
    if ctx.identification() != None or ctx.group() != None:
        if ctx.identification() != None and ctx.children[0] == ctx.identification():
            id += self.identification(ctx.identification())
        if ctx.group() != None:
            id += "(param)"
            group = ctx.group()
            groups = [group]
        if ctx.identification() != None and ctx.children[0] != ctx.identification():
            id += self.identification(ctx.identification())
        (rest_id, rest_groups) = get_execution_data(self,
                                                    ctx.execution_function_name2())
        groups = groups + rest_groups
        id += rest_id
    return (id, groups)


def get_definition_data(self, ctx):
    id = ""
    parameters = []
    if ctx.identification() != None or ctx.parameters() != None:
        if ctx.identification() != None and ctx.children[0] == ctx.identification():
            id += self.identification(ctx.identification())
        if ctx.parameters() != None:
            id += "(param)"
            parameter = ctx.parameters()
            parameters = [parameter]
        if ctx.identification() != None and ctx.children[0] != ctx.identification():
            id += self.identification(ctx.identification())
        (rest_id, rest_parameters) = get_definition_data(
            self, ctx.definition_function_name2())
        parameters = parameters + rest_parameters
        id += rest_id
    return (id, parameters)


def create_literal(self, ctx):
    if ctx.identification() != None:
        id = self.identification(ctx.identification())
        check_variable_exits(id)
        return gl.get_all_variables()[id]
    elif ctx.execution() != None:
        (function_name, virtual_direction) = self.execution(ctx.execution())
        exection_type = gl.functions[function_name].type
        return Variable("", exection_type, virtual_direction)
    elif ctx.String() != None:
        memory.add_constant(ctx.String().getText(), "STRING")
        return Variable("", "STRING", memory.get_last_constant() - 1)
    elif ctx.Boolean() != None:
        memory.add_constant(ctx.Boolean().getText(), "BOOLEAN")
        return Variable("", "BOOLEAN", memory.get_last_constant() - 1)
    elif ctx.Number() != None:
        memory.add_constant(ctx.Number().getText(), "NUMBER")
        return Variable("", "NUMBER", memory.get_last_constant() - 1)
    elif ctx.Empty() != None:
        memory.add_constant(None, "ANY")
        return Variable("", "ANY", memory.get_last_constant() - 1)
