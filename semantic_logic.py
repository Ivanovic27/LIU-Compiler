from preloaded_data import mapping_functions
from Cuadruple import Cuadruple
import copy

def get_id(self, ctx):
    id = ctx.Id()
    if id != None:
        rest_id = get_id(self, ctx.identification2())
        return str(id) + rest_id
    return ''


def check_return_type(self, function, return_literal):
    if function["type"] != None and function["type"] != return_literal["type"]:
        raise ValueError("Return type of function '" +
                         self.current_scope + "' is of type " + function["type"])
    function["type"] = return_literal["type"]


def check_defined_function(self, function_name):
    if function_name in self.functions:
        raise ValueError("The function '" + function_name +
                         "' is already defined")


def check_function_exists(self, table, function_name):
    for row in table:
        parameters = self.functions[function_name]["parameters"]
        a = False
        if "infiniteParams" in self.functions[function_name]:
            id = next(iter(parameters))
            a = parameters[id]["type"] == row["type"]
        else:
            for key, parameter in parameters.items():
                if(parameter["pos"] == row["pos"] and parameter["type"] == row["type"] and parameter["param"] == row["param"]):
                    a = True
                    break
        if(a == False):
            raise ValueError("Parameters of function '" +
                             function_name + "' do not match")
    # Check that function does not exist
    if(function_name not in self.functions):
        raise ValueError("Function " + function_name + "does not exist.")


def check_variable_exits(self, id):
    # Check if the accessed variable exists
    if id not in self.get_all_variables():
        raise ValueError(
            "'" + id + "' is not declared as a definition.")


def add_cuadruple_infinite(self, id, table):
    if len(table) == 0:
        registry = 't' + str(self.register)
        self.cuadruples.append(Cuadruple(id, None, None, registry))
        temp = registry
        self.register += 1
    else:
        temp = table[0]['name']

        if len(table) == 1:
            registry = 't' + str(self.register)
            self.cuadruples.append(Cuadruple(id, temp, None, registry))
            temp = registry
            self.register += 1
        for row in table[1:]:
            registry = 't' + str(self.register)
            self.cuadruples.append(Cuadruple(id, temp, row['name'], registry))
            temp = registry
            self.register += 1
    return temp


def create_function(self, ctx, function_name, parameters):
    # Ensure the new function is not already defined
    check_defined_function(self, function_name)
    # Add the function to the functions table
    self.functions[function_name] = {
        "type": None,
        "variables": {},
        "parameters": parameters
    }
    # Change scope inside of the new function
    self.current_scope = function_name
    self.function(ctx.function())
    self.current_scope = "global-function"


def create_variable(self, variable_name, literal):
    check_variable_type(self, variable_name, literal)
    # Add if is not already defined in other part
    if variable_name not in self.get_all_variables():
        self.get_variables()[variable_name] = {
            **literal, "name": variable_name}

def check_variable_type(self, variable_name, literal):
    # Check if the new variable type is different from the one already defined
    if variable_name in self.get_all_variables():
        if self.get_all_variables()[variable_name]["type"] != literal["type"]:
            raise ValueError("Type of definition '" + variable_name +
                             "' is not compatible with type " + literal["type"])

def get_group_variables(self, ctx, current_position=0):
    if ctx.literal() != None:
        item = self.literal(ctx.literal())
        item = copy.deepcopy(item)
        item["pos"] = current_position
        rest_items = get_group_variables(
            self, ctx.group3(), current_position + 1)
        return [item] + rest_items
    return []


def get_execution_data(self, ctx):
    id = ""
    groups = []
    if ctx.identification() != None or ctx.group() != None:
        (rest_id, rest_groups) = get_execution_data(self,
                                                    ctx.execution_function_name2())
        groups = rest_groups
        if ctx.identification() != None:
            id += self.identification(ctx.identification())
        if ctx.group() != None:
            id += '(param)'
            group = ctx.group()
            groups = [group] + groups
        id += rest_id
    return (id, groups)


def do_execution(self, groups, function_name, operation):
    parameters = []
    for index, group in enumerate(groups):
        current_parameters = self.group(group)
        current_parameters = current_parameters["variables"]
        for parameter in current_parameters:
            parameter["param"] = index
        parameters.extend(current_parameters)
    check_function_exists(self, parameters, function_name)
    return (function_name, add_cuadruple_infinite(self, operation, parameters))


def do_default_execution(self, ctx):
    for name, operation in mapping_functions.items():
        if getattr(ctx, name) and getattr(ctx, name)() != None:
            new_ctx = getattr(ctx, name)()
            groups = new_ctx.group()
            if not isinstance(groups, (list)):
                groups = [new_ctx.group()]
            return do_execution(self, groups, operation["name"], operation["operation"])


def check_global_function(self):
    if self.current_scope != "global-function":
        raise ValueError(
            'Function cannot be declared inside another function')


def get_parameters_data(self, ctx, param_position=0):
    parameters = {}
    if ctx.definition() != None:
        (name, type) = self.defintion_parameter(ctx.definition())
        parameters = get_parameters_data(
            self, ctx.parameters2(), param_position + 1)
        parameters[name] = {**type, "pos": param_position}
    return parameters


def list_params_to_dict(self, parameters):
    new_params = {}
    for index, parameter in enumerate(parameters):
        for key, param in parameter.items():
            param["param"] = index
            new_params[key] = param
    return new_params


def get_definition_data(self, ctx):
    id = ""
    parameters = []
    if ctx.identification() != None or ctx.parameters() != None:
        (rest_id, rest_parameters) = get_definition_data(
            self, ctx.definition_function_name2())
        parameters = rest_parameters
        if ctx.identification() != None:
            id += self.identification(ctx.identification())
        if ctx.parameters() != None:
            id += '(param)'
            parameter = self.parameters(ctx.parameters())
            parameters = [parameter] + parameters
        id += rest_id
    return (id, parameters)
