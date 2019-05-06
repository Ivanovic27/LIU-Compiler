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
    "max(param)": Function("max(param)", "NUMBER", {}, {
        "a": GroupItem("LIST", 0, None, 0),
    }),
    "min(param)": Function("min(param)", "NUMBER", {}, {
        "a": GroupItem("LIST", 0, None, 0),
    }),
    "(param)multiplyall": Function("(param)multiplyall", "NUMBER", {}, {
        "a": GroupItem("LIST", 0, None, 0),
    }),
    "(param)subtractall": Function("(param)subtractall", "NUMBER", {}, {
        "a": GroupItem("LIST", 0, None, 0),
    }),
    "(param)addall": Function("(param)addall", "NUMBER", {}, {
        "a": GroupItem("LIST", 0, None, 0),
    }),
    "(param)first": Function("(param)first", "ANY", {}, {
        "a": GroupItem("LIST", 0, None, 0),
    }),
    "(param)last": Function("(param)last", "ANY", {}, {
        "a": GroupItem("LIST", 0, None, 0),
    }),
    "(param)istext": Function("(param)istext", "BOOLEAN", {}, {
        "a": GroupItem("ANY", 0, None, 0),
    }),
    "(param)isnumber": Function("(param)isnumber", "BOOLEAN", {}, {
        "a": GroupItem("ANY", 0, None, 0),
    }),
    "(param)iseven": Function("(param)iseven", "BOOLEAN", {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
    }),
    "(param)isodd": Function("(param)isodd", "BOOLEAN", {}, {
        "a": GroupItem("NUMBER", 0, None, 0),
    }),
    "(param)isempty": Function("(param)isempty", "BOOLEAN", {}, {
        "a": GroupItem("ANY", 0, None, 0),
    }),
    "(param)map(param)": Function("(param)map(param)", "ANY", {}, {
        "a": GroupItem("LIST", 0, None, 0),
        "b": GroupItem("STRING", 0, None, 1),
        "c": GroupItem("NUMBER", 1, None, 1),
    }),
    "(param)filter(param)": Function("(param)filter(param)", "ANY", {}, {
        "a": GroupItem("LIST", 0, None, 0),
        "b": GroupItem("STRING", 0, None, 1),
        "c": GroupItem("NUMBER", 1, None, 1),
    }),
    "(param)length": Function("(param)length", "NUMBER", {}, {
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
    "multiply_all_execution": {"name": "(param)multiplyall", "type": "array", "operation": Operator.MULTIPLYALL},
    "subtract_all_execution": {"name": "(param)subtractall", "type": "array", "operation": Operator.SUBTRACTALL},
    "add_all_execution": {"name": "(param)addall", "type": "array", "operation": Operator.ADDALL},
    "first_execution": {"name": "(param)first", "type": "array", "operation": Operator.FIRST},
    "last_execution": {"name": "(param)last", "type": "array", "operation": Operator.LAST},
    "is_text_execution": {"name": "(param)istext", "type": "both", "operation": Operator.ISTEXT},
    "is_number_execution": {"name": "(param)isnumber", "type": "both", "operation": Operator.ISNUMBER},
    "is_odd_execution": {"name": "(param)isodd", "type": "both", "operation": Operator.ISODD},
    "is_even_execution": {"name": "(param)iseven", "type": "both", "operation": Operator.ISEVEN},
    "is_empty_execution": {"name": "(param)isempty", "type": "both", "operation": Operator.ISEMPTY},
    "map_execution": {"name": "(param)map(param)", "type": "map", "operation": Operator.MAP},
    "filter_execution": {"name": "(param)filter(param)", "type": "map", "operation": Operator.FILTER},
    "length_execution": {"name": "(param)length", "type": "array", "operation": Operator.LENGTH},
}
