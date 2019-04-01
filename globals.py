from preloaded_data import (initial_functions, initial_scope)
from beautifultable import BeautifulTable
import yaml

functions = initial_functions
current_register = 0
cuadruples = []
current_scope = initial_scope


def get_variables():
    return functions[current_scope]["variables"]


def get_global_variables():
    return functions["global-function"]["variables"]


def get_parameters():
    return functions[current_scope]["parameters"]


def get_all_variables():
    scope_variables = get_variables()
    params_variables = get_parameters()
    global_variables = get_global_variables()
    return {**global_variables, **params_variables, **scope_variables}


def get_current_function():
    return functions[current_scope]


def print_cuadruples():
    table = BeautifulTable()
    table.column_headers = ["operator", "right", "left", "temporal"]
    for cuadruple in cuadruples:
        table.append_row([cuadruple.operator, cuadruple.left,
                          cuadruple.right, cuadruple.temporal])
    print(table)


def print_all_functions():
    print(yaml.dump(functions))


def print_function(function_name):
    print(yaml.dump(functions[function_name]))
