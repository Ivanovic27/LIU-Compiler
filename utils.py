
def array_params_to_dict(parameters):
    """
    Name: array_params_to_dict
    Description: Converts an array to a dictionary
    Parameters: parameters: the list of all parameters to be converted to a dictionary.
    Returns: The parameters as a dictionary
    Important methods where its called:
    - definition_function_parameters: to convert the list of parameters to a dictionary.
    """
    new_params = {}
    for index, parameter in enumerate(parameters):
        for key, param in parameter.items():
            param.param = index
            new_params[key] = param
    return new_params
