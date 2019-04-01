
def list_params_to_dict(parameters):
    new_params = {}
    for index, parameter in enumerate(parameters):
        for key, param in parameter.items():
            param["param"] = index
            new_params[key] = param
    return new_params
