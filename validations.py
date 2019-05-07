from globals import (global_data as gl)
from preloaded_data import global_function


def check_return_type(function, return_literal):
    if function.type != 'ANY' and return_literal.type != 'ANY' and function.type != None and function.type != return_literal.type:
        raise ValueError("Return type of function '" +
                         gl.current_scope + "' is of type " + str(function.type))
    function.type = return_literal.type


def check_defined_function(function_name):
    if function_name in gl.functions:
        raise ValueError("The function '" + function_name +
                         "' is already defined")


def check_function_match(arguments, function_name):
    """
    Name: check_function_match
    Description: Checks if the name of the function and its parameters match.
    Parameters:
        arguments: Holds all the arguments of the function. 
        function_name: The name of the function to be validated.
    Returns: NA.
    Important methods where its called:
        execution_function_name: To execute a user definied function.
    """
    for argument in arguments:
        parameters = gl.functions[function_name].parameters
        match = False
        if gl.functions[function_name].infiniteParams:
            id = next(iter(parameters))
            match = parameters[
                id].type == 'ANY' or argument.type == 'ANY' or parameters[
                id].type == argument.type
        else:
            for _, parameter in parameters.items():
                if parameter.type == 'ANY' or argument.type == 'ANY' or parameter.pos == argument.pos and parameter.type == argument.type and parameter.param == argument.param:
                    match = True
                    break
        if not match:
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
                raise ValueError("Type of definition '" + str(variable_name) +
                                 "' is not compatible with type " + str(literal.type))
