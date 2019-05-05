from Function import Function
from GroupItem import GroupItem
from Operator import Operator

global_function = "global-function"
initial_scope = "global-function"
initial_functions = {
    "global-function": Function("global-function", "EMPTY", {}, {}),
    "add(param)": Function("add(param)", "NUMBER", {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
        "b": GroupItem("NUMBER", 1, None, 0),
    }, True),
    "subtract(param)": Function("subtract(param)", "NUMBER", {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
        "b": GroupItem("NUMBER", 1, None, 0),
    }, True),
    "divide(param)": Function("divide(param)", "NUMBER", {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
        "b": GroupItem("NUMBER", 1, None, 0),
    }, True),
    "multiply(param)": Function("multiply(param)", "NUMBER", {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
        "b": GroupItem("NUMBER", 1, None, 0),
    }, True),
    "sqrt(param)": Function("sqrt(param)", "NUMBER", {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
    }),
    "(param)power(param)": Function("(param)power(param)", "NUMBER", {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
        "b": GroupItem("NUMBER", 0, None, 1),
    }),
    "not(param)": Function("not(param)", "BOOLEAN", {}, {
        "a": GroupItem("BOOLEAN", 0, None, 0),
    }, False),
    "equal(param)": Function("equal(param)", "BOOLEAN", {}, {
        "a": GroupItem("ANY", 0, None, 0),
        "b": GroupItem("ANY", 1, None, 0),
    }),
    "greater(param)": Function("greater(param)", "BOOLEAN", {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
        "b": GroupItem("NUMBER", 1, None, 0),
    }),
    "less(param)": Function("less(param)", "BOOLEAN", {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
        "b": GroupItem("NUMBER", 1, None, 0),
    }),
    "or(param)": Function("or(param)", "BOOLEAN", {}, {
        "a": GroupItem("BOOLEAN", 0, None, 0),
    }, True),
    "and(param)": Function("and(param)", "BOOLEAN", {}, {
        "a": GroupItem("BOOLEAN", 0, None, 0),
    }, True),
    "print(param)": Function("print(param)", "EMPTY", {}, {
        "a": GroupItem("ANY", 0, None, 0),
    }, True),
    "read(param)": Function("read(param)", "ANY", {}, {}),
    "if(param)": Function("if(param)", "EMPTY", {}, {
        "a": GroupItem("BOOLEAN", 0, None, 0),
    }),
    "iteratewhile(param)": Function("iteratewhile(param)", "EMPTY", {}, {
        "a": GroupItem("BOOLEAN", 0, None, 0),
    }),
    "max(param)": Function("max(param)", "EMPTY", {}, {
        "a": GroupItem("LIST", 0, None, 0),
    }),
    "min(param)": Function("min(param)", "EMPTY", {}, {
        "a": GroupItem("LIST", 0, None, 0),
    }),
}
mapping_functions = {
    "add_execution": {"name": "add(param)", "type": "both", "operation": Operator.SUM},
    "subtract_execution": {"name": "subtract(param)", "type": "both", "operation": Operator.SUBTRACT},
    "divide_execution": {"name": "divide(param)", "type": "both", "operation": Operator.DIVIDE},
    "multiply_execution": {"name": "multiply(param)", "type": "both", "operation": Operator.MULTIPLY},
    "not_execution": {"name": "not(param)", "type": "both", "operation": Operator.NOT},
    "equal_execution": {"name": "equal(param)", "type": "both", "operation": Operator.EQUAL},
    "greater_execution": {"name": "greater(param)", "type": "both", "operation": Operator.GREATER},
    "less_execution": {"name": "less(param)", "type": "both", "operation": Operator.LESS},
    "or_execution": {"name": "or(param)", "type": "both", "operation": Operator.OR},
    "and_execution": {"name": "and(param)", "type": "both", "operation": Operator.AND},
    "print_execution": {"name": "print(param)", "type": "left", "operation": Operator.PRINT},
    "read_execution": {"name": "read(param)", "type": "both", "operation": Operator.READ},
    "sqrt_execution": {"name": "sqrt(param)", "type": "both", "operation": Operator.SQRT},
    "power_execution": {"name": "(param)power(param)", "type": "both", "operation": Operator.POWER},
    "max_execution": {"name": "max(param)", "type": "array", "operation": Operator.MAX},
    "min_execution": {"name": "min(param)", "type": "array", "operation": Operator.MIN},
}
