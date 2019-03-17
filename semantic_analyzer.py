from antlr4 import *
from semantic_logic import function_code
import json


class LiuGrammarListener(ParseTreeListener):
    def enterProgram(self, ctx):
        pass


class SemanticAnalyzer(LiuGrammarListener):
    def __init__(self):
        self.functions = {
            "global-function": {"type": None, "variables": {}, "parameters": {}}
        }
        self.current_scope = "global-function"

    def enterProgram(self, ctx):
        function_code(self, ctx.function_code())
        print(json.dumps(self.functions, indent=2))
