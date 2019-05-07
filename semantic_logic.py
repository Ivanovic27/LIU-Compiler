from preloaded_data import mapping_functions
import copy
from preloaded_data import global_function
from globals import (global_data as gl, memory)
from validations import *
from Function import Function
from Variable import Variable
from GroupItem import GroupItem
from utils import array_params_to_dict
from Operator import Operator

# Redirects to the mehtod depending on the type of quadruples a function has to generate.
types = {
    "both": gl.add_continuous_quadruples,
    "left": gl.add_left_quadruples,
    "array": gl.add_array_quadruple,
    "map": gl.add_map_quadruple
}


def create_variable(variable_name, literal):
    """
    Name: create_variable
    Description: Creates a variable in the current scope.
    Parameters:
        variable_name: The name of the variable to create.
        literal: The information of the content of the variable.
    Returns: NA
    Important methods where its called:
        definition_variable: To define an array or variable.
    """
    check_variable_type(variable_name, literal)
    variable = gl.get_variable(variable_name)
    if not variable:
        # Add variable if not already declared.
        new_dir = gl.get_last_data()
        if literal.type == 'LIST':
            (size, _, _) = literal.array_info
            literal.virtual_direction = new_dir
            literal.name = variable_name
            literal.constant_direction = memory.get_last_constant()
            memory.add_constant(new_dir, 'NUMBER')
            new_variable = literal
            for _ in range(0, size):
                gl.add_memory(None)
        else:
            gl.add_memory(None)
            new_variable = Variable(variable_name, literal.type, new_dir)
        gl.add_variable(variable_name, new_variable)
        variable = gl.get_variable(variable_name)
    else:
        if literal.type == 'LIST':
            new_dir = gl.get_last_data()
            (size, _, _) = literal.array_info
            literal.virtual_direction = new_dir
            literal.name = variable_name
            literal.constant_direction = memory.get_last_constant()
            memory.add_constant(new_dir, 'NUMBER')
            new_variable = literal
            for _ in range(0, size):
                gl.add_memory(None)
            gl.add_variable(variable_name, new_variable)
            variable = gl.get_variable(variable_name)
    if literal.type != 'LIST':
        memory.add_assign(literal.virtual_direction,
                          variable.virtual_direction)


def definition_function_parameters(self, ctx, parameters):
    """
    Name: definition_function_parameters
    Description: Gets all the parameters of a function.
    Parameters:
        ctx: Holds the context of the parameters rule.
    Returns: All the parameters information of a function.
    Important methods where its called:
        definition_function: To hold all the parameters of the function.
    """
    counter = 0
    new_parameters = []
    for param in parameters:
        new_parameters.append(self.parameters(param))
    for param in new_parameters:
        current_position = 0
        finish = False
        while not finish:
            found_item = False
            for (_, attr) in param.items():
                if attr.pos == current_position:
                    attr.global_pos = counter
                    counter += 1
                    current_position += 1
                    found_item = True
                    break
            if not found_item:
                finish = True
    return array_params_to_dict(new_parameters)


def do_function_execution(self, ctx):
    """
    Name: do_function_execution
    Description: Generates quadruples for user defined function calls.
    Parameters:
        ctx: Holds the context of the execution_function_name rule.
    Returns: The name of the function and its returned direction.
    Important methods where its called:
        execution_function_name: To execute a user definied function.
    """
    (function_name, grps) = get_execution_data(self, ctx)
    func = gl.functions[function_name]
    (new_function_name, groups) = prepare_arguments(
        self, grps, function_name)
    memory.add_quadruple(Operator.ERA, func.virtual_directon, None, None)
    parameters = gl.functions[function_name].parameters
    for group in groups:
        for key, parameter in parameters.items():
            if parameter.pos == group.pos and parameter.param == group.param:
                if parameter.type == 'LIST':
                    (_, _, size_dir) = parameter.array_info
                    memory.add_quadruple(
                        Operator.PARAMARR, group.virtual_direction, size_dir, parameter.virtual_direction)
                else:
                    memory.add_quadruple(
                        Operator.PARAM, group.virtual_direction, None, parameter.virtual_direction)
    memory.add_quadruple(Operator.GOSUB, func.code_direction, None, None)
    # aqui
    new_dir = gl.get_last_data()
    gl.add_memory(None)
    memory.add_quadruple(Operator.ASSIGN, func.return_direction, None, new_dir)
    return (new_function_name, new_dir)


def get_id(ctx):
    """
    Name: get_id
    Description: Gets the id. It can be built with spaces. Ex: 'important stuff'--> 'importantstuff'
    Parameters:
        ctx: Holds the context of the identification2 rule.
    Returns: The id of what was accessed.
    Important methods where its called:
        identification: To access the built id.
    """
    id = ctx.Id()
    if id != None:
        rest_id = get_id(ctx.identification2())
        return id.getText() + rest_id
    return ""


def create_function(self, ctx, function_name, parameters, initial_virtual_direction, literal, return_direction):
    """
    Name: create_function
    Description: Creates the information for the function with its corresponding quadruples.
    Parameters:
        ctx: Holds the context of the definition_function rule.
        function_name: The name of the function to create.
        parameters: The information of the parameters of the function.
        initial_virtual_direction: The virtual direction to access after Start Proc.
        literal: Information about the return literal.
        return_direction: The global direction used for the return.
    Returns: NA
    Important methods where its called:
        definition_function: To create the quadruples of the function.
    """
    # Ensure the new function is not already defined
    check_defined_function(function_name)
    code_virtual_direction = memory.get_last_code() + 1
    # Add the function to the functions table
    gl.functions[function_name] = Function(
        function_name, literal.type, {}, parameters, False, initial_virtual_direction, code_virtual_direction, return_direction, literal.array_info)
    memory.add_quadruple(Operator.PARAMEND, None, None, None)
    self.function(ctx.function())
    gl.current_scope = global_function
    memory.add_quadruple(Operator.ENDPROC, None, None, None)
    memory.local_segment.clear()


def get_group_variables(self, ctx, current_position=0):
    """
    Name: get_group_variables
    Description: Compiles part of the arguments of a function call.
    Parameters:
        ctx: Holds the context of the group2/group3 rule.
    Returns: NA
    Important methods where its called:
        get_group_variables: To get all the arguments inside a group
        group: Get the variables inside a group.
    """
    if ctx.basic_literal() != None:
        item = self.basic_literal(ctx.basic_literal())
        new_item = GroupItem(item.type, current_position,
                             item.virtual_direction, None, item.array_info)
        rest_items = get_group_variables(
            self, ctx.group3(), current_position + 1)
        return [new_item] + rest_items
    return []


def prepare_arguments(self, groups, function_name):
    """
    Name: prepare_arguments
    Description: Gets the data needed for all arguments.
    Parameters:
        groups: Holds all group contexts.
        function_name: The name of the function to be validated.
    Returns: The name of the function and its arguments on a array of groups.
    Important methods where its called:
        execution_function_name: To execute a user definied function.
    """
    arguments = []
    for index, group in enumerate(groups):
        current_arguments = self.group(group)
        current_arguments = current_arguments.variables
        for parameter in current_arguments:
            parameter.param = index
        arguments.extend(current_arguments)
    check_function_match(arguments, function_name)
    return (function_name, arguments)


def do_default_execution(self, ctx):
    """
    Name: do_default_execution
    Description: Generates the quadruples for common functions.
    Parameters:
        ctx: Holds the context of the execution rule.
    Returns: Returns the name of the function and the last virtual direction.
    Important methods where its called:
        execution: To execute common functions.
    """
    # Iterate all mapping functions until it finds one that exists in context
    for name, operation in mapping_functions.items():
        if getattr(ctx, name) and getattr(ctx, name)() != None:
            new_ctx = getattr(ctx, name)()
            groups = new_ctx.group()
            if not isinstance(groups, (list)):
                groups = [new_ctx.group()]
            (function_name, parameters) = prepare_arguments(
                self, groups, operation["name"])
            quadruple_function = types[operation["type"]]
            direction = quadruple_function(operation["operation"], parameters)
            return (function_name, direction)


def do_if_execution(self, ctx):
    """
    Name: do_if_execution
    Description: Generates the quadruples for the if statement.
    Parameters:
        ctx: Holds the context of the if_execution rule.
    Returns: NA
    Important methods where its called:
        if_execution: To execute an if statement.
        do_else_execution: To execute an if statement after an else.
    """
    function_name = "if(param)"
    (_, parameters) = prepare_arguments(
        self, [ctx.group()], function_name)
    condition_dir = parameters[0].virtual_direction
    memory.add_gotoFalse(condition_dir)
    gl.add_jump(-1)
    self.function(ctx.function())
    self.else_execution(ctx)


def do_else_execution(self, ctx):
    """
    Name: do_else_execution
    Description: Generates the quadruples for the else statement.
    Parameters:
        ctx: Holds the context of the else_execution rule.
    Returns: NA
    Important methods where its called:
        else_execution: To execute an else statement.
    """
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
    """
    Name: do_iterate_execution
    Description: Generates the quadruples for a while iterate statement.
    Parameters:
        ctx: Holds the context of the iterate_execution rule.
    Returns: NA
    Important methods where its called:
        iterate_execution: To execute an iterate statement.
    """
    function_name = "iteratewhile(param)"
    gl.add_jump()
    (_, parameters) = prepare_arguments(
        self, [ctx.group()], function_name)
    condition_dir = parameters[0].virtual_direction
    memory.add_gotoFalse(condition_dir)
    gl.add_jump(-1)
    self.function(ctx.function())
    begin_dir = gl.pending_jumps.pop()
    end_dir = gl.pending_jumps.pop()
    memory.add_goto(end_dir)
    memory.fill_jump(begin_dir)


def get_parameters_data(self, ctx, param_position=0):
    """
    Name: get_parameters_data
    Description: Retrieves the parameters of a group of a function.
    Parameters:
        ctx: Holds the context of the parameters3 rule.
    Returns: A list of all the parameters of a group.
    Important methods where its called:
        parameters: To get the information of the parameters of a group of a function.
    """
    parameters = {}
    if ctx.definition() != None:
        (name, literal, direction) = self.defintion_parameter(ctx.definition())
        parameters = get_parameters_data(
            self, ctx.parameters2(), param_position + 1)
        parameters[name] = GroupItem(
            literal.type, param_position, None, None, literal.array_info)
        if literal.type == 'LIST':
            parameters[name].constant_direction = literal.constant_direction
        parameters[name].virtual_direction = direction
    return parameters


def get_execution_data(self, ctx):
    """
    Name: get_execution_data
    Description: Gets both the name of the executed function and a array of all the passed parameters in order.
    Parameters:
        ctx: Holds the context of the execution_function_name rule.
    Returns: The name of the function in order and its parameters on a array.
    Important methods where its called:
        do_function_execution: To get the name of the function and its parameters in order
        get_execution_data: To get all the parameters
    """
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
    """
    Name: get_definition_data
    Description: Creates and gets information about the new funtion.
    Parameters:
        ctx: Holds the context of the definition_function_name rule.
    Returns: The name of the function and the context of the parameters.
    Important methods where its called:
        definition_function_name: To create information about the function.
        get_definition_data: To get all the parameters on the definition
    """
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
    """
    Name: create_literal
    Description: Gets or creates a literal adding it to memory (if needed).
    Parameters:
        ctx: Holds the context of the basic_literal rule.
    Returns: Information about a basic literal (string, number, etc).
    Important methods where its called:
        basic_literal: To create and get the information of a literal.
    """
    if ctx.identification() != None:
        id = self.identification(ctx.identification())
        check_variable_exits(id)
        return gl.get_all_variables()[id]
    elif ctx.array_access() != None:
        (id, direction) = self.array_access(ctx.array_access())
        return Variable("", 'ANY', direction)
    elif ctx.execution() != None:
        (function_name, virtual_direction) = self.execution(ctx.execution())
        exection_type = gl.functions[function_name].type
        array_info = gl.functions[function_name].return_array_info
        if virtual_direction == None:
            return_direction = gl.functions[function_name].return_direction
        else:
            return_direction = virtual_direction
        return Variable("", exection_type, return_direction, array_info)
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
