from globals import (global_data as gl)
from preloaded_data import global_function


def check_return_type(function, return_literal):
    if function.type != 'ANY' and return_literal.type != 'ANY' and function.type != None and function.type != return_literal.type:
        raise ValueError("Return type of function '" +
                         gl.current_scope + "' is of type " + function.type)
    function.type = return_literal.type


def check_defined_function(function_name):
    if function_name in gl.functions:
        raise ValueError("The function '" + function_name +
                         "' is already defined")


def check_function_exists(table, function_name):
    for row in table:
        parameters = gl.functions[function_name].parameters
        not_match = False
        if gl.functions[function_name].infiniteParams:
            id = next(iter(parameters))
            not_match = parameters[
                id].type == 'ANY' or row.type == 'ANY' or parameters[
                id].type == row.type
        else:
            for key, parameter in parameters.items():
                if parameter.type == 'ANY' or row.type == 'ANY' or parameter.pos == row.pos and parameter.type == row.type and parameter.param == row.param:
                    not_match = True
                    break
        if not_match == False:
            raise ValueError("Parameters of function '" +
                             function_name + "' do not match")
    # Check that function does not exist
    if function_name not in gl.functions:
        raise ValueError("Function " + function_name + "does not exist.")


def check_variable_exits(id):
    # Check if the accessed variable exists
    if id not in gl.get_all_variables():
        raise ValueError(
            "'" + id + "' is not declared as a definition.")


def check_global_function():
    if gl.current_scope != global_function:
        raise ValueError(
            "Function cannot be declared inside another function")


def check_variable_type(variable_name, literal):
    # Check if the new variable type is different from the one already defined
    if variable_name in gl.get_all_variables():
        if gl.get_all_variables()[variable_name].type != 'ANY' and literal.type != 'ANY':
            if gl.get_all_variables()[variable_name].type != literal.type:
                raise ValueError("Type of definition '" + variable_name +
                                 "' is not compatible with type " + literal.type)
