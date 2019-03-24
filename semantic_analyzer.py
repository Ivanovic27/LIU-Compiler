from antlr4 import *
from semantic_logic import function_code
import json
import yaml


class LiuGrammarListener(ParseTreeListener):
    def enterProgram(self, ctx):
        pass


class SemanticAnalyzer(LiuGrammarListener):
    def __init__(self):
        self.functions = {
            "global-function": {"type": None, "variables": {}, "parameters": {}},
            "sum(param)": {
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
                    "a": {"type": "STRING", "param": 0, "pos": 0},
                }
            },
        }
        self.register = 0
        self.cuadruples = []
        self.current_scope = "global-function"

    def enterProgram(self, ctx):
        function_code(self, ctx.function_code())
        # print(yaml.dump(self.functions))
        print(json.dumps(self.functions, indent=2))
        print(json.dumps(self.cuadruples, indent=2))
