from Function import Function
from GroupItem import GroupItem

global_function = "global-function"
initial_scope = "global-function"
initial_functions = {
    "global-function": Function('global-function', 'NONE', {}, {}),
    "add(param)": Function('add(param)', 'NUMBER', {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
        "b": GroupItem("NUMBER", 1, None, 0),
    }, True),
    "subtract(param)": Function('subtract(param)', 'NUMBER', {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
        "b": GroupItem("NUMBER", 1, None, 0),
    }, True),
    "divide(param)": Function('divide(param)', 'NUMBER', {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
        "b": GroupItem("NUMBER", 1, None, 0),
    }, True),
    "multiply(param)": Function('multiply(param)', 'NUMBER', {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
        "b": GroupItem("NUMBER", 1, None, 0),
    }, True),
    "not(param)": Function('not(param)', 'BOOLEAN', {}, {
        "a": GroupItem("BOOLEAN", 0, None, 0),
    }, False),
    "equal(param)": Function('equal(param)', 'BOOLEAN', {}, {
        "a": GroupItem("STRING", 0, None, 0),
    }, True),
    "or(param)": Function('or(param)', 'BOOLEAN', {}, {
        "a": GroupItem("BOOLEAN", 0, None, 0),
    }, True),
    "and(param)": Function('and(param)', 'BOOLEAN', {}, {
        "a": GroupItem("BOOLEAN", 0, None, 0),
    }, True),
    "print(param)": Function('print(param)', 'NONE', {}, {
        "a": GroupItem("STRING", 0, None, 0),
    }, True),
    "read(param)": Function('read(param)', 'NONE', {}, {}),
    "if(param)": Function('if(param)', 'NONE', {}, {
        "a": GroupItem("BOOLEAN", 0, None, 0),
    }),
    "iteratewhile(param)": Function('iteratewhile(param)', 'NONE', {}, {
        "a": GroupItem("BOOLEAN", 0, None, 0),
    }),
}
mapping_functions = {
    "add_execution": {"name": "add(param)", "operation": "+"},
    "subtract_execution": {"name": "subtract(param)", "operation": "-"},
    "divide_execution": {"name": "divide(param)", "operation": "/"},
    "multiply_execution": {"name": "multiply(param)", "operation": "*"},
    "not_execution": {"name": "not(param)", "operation": "not"},
    "equal_execution": {"name": "equal(param)", "operation": "equal"},
    "or_execution": {"name": "or(param)", "operation": "or"},
    "and_execution": {"name": "and(param)", "operation": "and"},
    "print_execution": {"name": "print(param)", "operation": "print"},
    "read_execution": {"name": "read(param)", "operation": "read"},
}
