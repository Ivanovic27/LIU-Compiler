initial_scope = "global-function"
initial_functions = {
    "global-function": {"type": None, "variables": {}, "parameters": {}},
    "add(param)": {
        "type": "NUMBER",
        "variables": {},
        "infiniteParams": True,
        "parameters": {
            "a": {"type": "NUMBER", "param": 0, "pos": 0},
            "b": {"type": "NUMBER", "param": 0, "pos": 1}
        }
    },
    "subtract(param)": {
        "type": "NUMBER",
        "variables": {},
        "infiniteParams": True,
        "parameters": {
            "a": {"type": "NUMBER", "param": 0, "pos": 0},
            "b": {"type": "NUMBER", "param": 0, "pos": 1}
        }
    },
    "divide(param)": {
        "type": "NUMBER",
        "variables": {},
        "parameters": {
            "a": {"type": "NUMBER", "param": 0, "pos": 0},
            "b": {"type": "NUMBER", "param": 0, "pos": 1}
        }
    },
    "multiply(param)": {
        "type": "NUMBER",
        "variables": {},
        "infiniteParams": True,
        "parameters": {
            "a": {"type": "NUMBER", "param": 0, "pos": 0},
            "b": {"type": "NUMBER", "param": 0, "pos": 1}
        }
    },
    "not(param)": {
        "type": "BOOLEAN",
        "variables": {},
        "parameters": {
            "a": {"type": "BOOLEAN", "param": 0, "pos": 0},
        }
    },
    "equal(param)": {
        "type": "BOOLEAN",
        "variables": {},
        "infiniteParams": True,
        "parameters": {
            "a": {"type": "STRING", "param": 0, "pos": 0},
        }
    },
    "or(param)": {
        "type": "BOOLEAN",
        "variables": {},
        "infiniteParams": True,
        "parameters": {
            "a": {"type": "BOOLEAN", "param": 0, "pos": 0},
        }
    },
    "and(param)": {
        "type": "BOOLEAN",
        "variables": {},
        "infiniteParams": True,
        "parameters": {
            "a": {"type": "BOOLEAN", "param": 0, "pos": 0},
        }
    },
    "print(param)": {
        "type": "NONE",
        "variables": {},
        "infiniteParams": True,
        "parameters": {
            "a": {"type": "STRING", "param": 0, "pos": 0},
        }
    },
    "read(param)": {
        "type": "NONE",
        "variables": {},
        "parameters": {
        }
    },
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
