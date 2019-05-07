from globals import (global_data as gl)
from preloaded_data import global_function


def check_return_type(function, return_literal):
    """
    Name: check_return_type
    Description: Validates that the return type is the same as the one previously defined.
    Parameters:
        function: The function that is beeing accessed.
        return_literal: The literal that was returned.
    Returns: Throws error if not correctly.
    Important methods where its called:
        return_statement: To validate the return type is correct.
    """
    if function.type != 'ANY' and return_literal.type != 'ANY' and function.type != None and function.type != return_literal.type:
        raise ValueError("Return type of function '" +
                         gl.current_scope + "' is of type " + str(function.type))
    if function.type != 'ANY' and return_literal.type != 'ANY':
        function.type = return_literal.type


def check_defined_function(function_name):
    """
    Name: check_defined_function
    Description: Validates that the accessed function exists.
    Parameters:
        function_name: The name of the function to validate.
    Returns: Throws error if not correctly.
    Important methods where its called:
        create_function: To check the defined function is a new one.
    """
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
    """
    Name: check_variable_exits
    Description: Validates that the accessed variable exists.
    Parameters:
        id: The variable name to check if exists globally or locally.
    Returns: Throws error if not correctly.
    Important methods where its called:
        create_literal: To check if accessed literal exists as a variable.
        array_access: To check if an accessed array exists as a variable.
    """
    if id not in gl.get_all_variables():
        raise ValueError(
            "'" + id + "' is not declared as a definition.")


def check_global_function():
    """
    Name: check_global_function
    Description: Validates that the function is globally declared.
    Parameters:
    Returns: Throws error if not correctly.
    Important methods where its called:
        definition_function_name: To check when defining a new function.
    """
    if gl.current_scope != global_function:
        raise ValueError(
            "Function cannot be declared inside another function")


def check_variable_type(variable_name, literal):
    """
    Name: check_variable_type
    Description: Validates that the the new variable type is the same as the one already defined.
    Parameters:
        variable_name: The variable to check if is the same type.
        literal: The literal with a certain type.
    Returns: Throws error if not correctly.
    Important methods where its called:
        create_variable: To check the type when assinging the a value to the variable.
    """
    if variable_name in gl.get_all_variables():
        if gl.get_all_variables()[variable_name].type != 'ANY' and literal.type != 'ANY':
            if gl.get_all_variables()[variable_name].type != literal.type:
                raise ValueError("Type of definition '" + str(variable_name) +
                                 "' is not compatible with type " + str(literal.type))
