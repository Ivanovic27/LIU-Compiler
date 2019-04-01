from preloaded_data import mapping_functions
from Cuadruple import Cuadruple
import copy
import globals as gl
from validations import *


def add_cuadruple_infinite(id, table):
    if len(table) == 0:
        registry = 't' + str(gl.current_register)
        gl.cuadruples.append(Cuadruple(id, None, None, registry))
        temp = registry
        gl.current_register += 1
    else:
        temp = table[0]['name']

        if len(table) == 1:
            registry = 't' + str(gl.current_register)
            gl.cuadruples.append(Cuadruple(id, temp, None, registry))
            temp = registry
            gl.current_register += 1
        for row in table[1:]:
            registry = 't' + str(gl.current_register)
            gl.cuadruples.append(Cuadruple(id, temp, row['name'], registry))
            temp = registry
            gl.current_register += 1
    return temp


def create_variable(variable_name, literal):
    check_variable_type(variable_name, literal)
    # Add if is not already defined in other part
    if variable_name not in gl.get_all_variables():
        gl.get_variables()[variable_name] = {
            **literal, "name": variable_name}

def get_id(ctx):
    id = ctx.Id()
    if id != None:
        rest_id = get_id(ctx.identification2())
        return str(id) + rest_id
    return ''


def create_function(self, ctx, function_name, parameters):
    # Ensure the new function is not already defined
    check_defined_function(function_name)
    # Add the function to the functions table
    gl.functions[function_name] = {
        "type": None,
        "variables": {},
        "parameters": parameters
    }
    # Change scope inside of the new function
    gl.current_scope = function_name
    self.function(ctx.function())
    gl.current_scope = "global-function"

def get_group_variables(self, ctx, current_position=0):
    if ctx.literal() != None:
        item = self.literal(ctx.literal())
        item = copy.deepcopy(item)
        item["pos"] = current_position
        rest_items = get_group_variables(
            self, ctx.group3(), current_position + 1)
        return [item] + rest_items
    return []


def do_execution(self, groups, function_name, operation):
    parameters = []
    for index, group in enumerate(groups):
        current_parameters = self.group(group)
        current_parameters = current_parameters["variables"]
        for parameter in current_parameters:
            parameter["param"] = index
        parameters.extend(current_parameters)
    check_function_exists(parameters, function_name)
    return (function_name, add_cuadruple_infinite(operation, parameters))


def do_default_execution(self, ctx):
    for name, operation in mapping_functions.items():
        if getattr(ctx, name) and getattr(ctx, name)() != None:
            new_ctx = getattr(ctx, name)()
            groups = new_ctx.group()
            if not isinstance(groups, (list)):
                groups = [new_ctx.group()]
            return do_execution(self, groups, operation["name"], operation["operation"])


def get_parameters_data(self, ctx, param_position=0):
    parameters = {}
    if ctx.definition() != None:
        (name, type) = self.defintion_parameter(ctx.definition())
        parameters = get_parameters_data(
            self, ctx.parameters2(), param_position + 1)
        parameters[name] = {**type, "pos": param_position}
    return parameters


def get_execution_data(self, ctx):
    id = ""
    groups = []
    if ctx.identification() != None or ctx.group() != None:
        (rest_id, rest_groups) = get_execution_data(self,
                                                    ctx.execution_function_name2())
        groups = rest_groups
        if ctx.identification() != None and ctx.children[0] == ctx.identification():
            id += self.identification(ctx.identification())
        if ctx.group() != None:
            id += '(param)'
            group = ctx.group()
            groups = [group] + groups
        if ctx.identification() != None and ctx.children[0] != ctx.identification():
            id += self.identification(ctx.identification())
        id += rest_id
    return (id, groups)

def get_definition_data(self, ctx):
    id = ""
    parameters = []
    if ctx.identification() != None or ctx.parameters() != None:
        (rest_id, rest_parameters) = get_definition_data(
            self, ctx.definition_function_name2())
        parameters = rest_parameters
        if ctx.identification() != None and ctx.children[0] == ctx.identification():
            id += self.identification(ctx.identification())
        if ctx.parameters() != None:
            id += '(param)'
            parameter = self.parameters(ctx.parameters())
            parameters = [parameter] + parameters
        if ctx.identification() != None and ctx.children[0] != ctx.identification():
            id += self.identification(ctx.identification())
        id += rest_id
    return (id, parameters)
