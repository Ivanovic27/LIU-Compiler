from antlr4 import *
import yaml
from preloaded_data import (initial_functions, initial_scope)
from beautifultable import BeautifulTable
from semantic_logic import *
import copy


class LiuGrammarListener(ParseTreeListener):
    def enterProgram(self, ctx):
        pass


class SemanticAnalyzer(LiuGrammarListener):
    def __init__(self):
        self.functions = initial_functions
        self.register = 0
        self.cuadruples = []
        self.current_scope = initial_scope

    def enterProgram(self, ctx):
        self.function_code(ctx.function_code())

        self.print_function("global-function")
        self.print_function("a(param)do(param)")
        self.print_cuadruples()

    def print_cuadruples(self):
        table = BeautifulTable()
        table.column_headers = ["operator", "right", "left", "temporal"]
        for cuadruple in self.cuadruples:
            table.append_row([cuadruple.operator, cuadruple.left,
                              cuadruple.right, cuadruple.temporal])
        print(table)

    def get_current_function(self):
        return self.functions[self.current_scope]

    def print_function(self, function_name):
        print(yaml.dump(self.functions[function_name]))

    def get_variables(self):
        return self.functions[self.current_scope]["variables"]

    def get_global_variables(self):
        return self.functions["global-function"]["variables"]

    def get_parameters(self):
        return self.functions[self.current_scope]["parameters"]

    def get_all_variables(self):
        scope_variables = self.get_variables()
        params_variables = self.get_parameters()
        global_variables = self.get_global_variables()
        return {**global_variables, **params_variables, **scope_variables}

    def identification(self, ctx):
        return get_id(self, ctx)

    def function(self, ctx):
        self.function_code(ctx.function_code())

    def function_code(self, ctx):
        if ctx.instruction() != None:
            self.instruction(ctx.instruction())
            self.function_code(ctx.function_code())

    def instruction(self, ctx):
        if ctx.definition() != None:
            self.definition(ctx.definition())
        elif ctx.execution() != None:
            self.execution(ctx.execution())
        elif ctx.return_statement() != None:
            self.return_statement(ctx.return_statement())

    def definition(self, ctx):
        if ctx.definition_function_name():
            self.definition_function(ctx)
        else:
            self.definition_variable(ctx)

    def execution(self, ctx):
        if ctx.execution_function_name() != None:
            (function_name, groups) = self.execution_function_name(
                ctx.execution_function_name())
            return do_execution(self, groups, function_name, function_name)
        else:
            return do_default_execution(self, ctx)

    def return_statement(self, ctx):
        if ctx.group() != None:
            return_literal = self.group(ctx.group())
        else:
            return_literal = self.basic_literal(ctx.basic_literal())
        current_function = self.get_current_function()
        check_return_type(self, current_function, return_literal)

    def definition_function(self, ctx):
        (function_name, parameters) = self.definition_function_name(
            ctx.definition_function_name())
        create_function(self, ctx, function_name, parameters)

    def definition_variable(self, ctx):
        variable_name = self.identification(ctx.identification())
        literal = self.extended_literal(ctx.extended_literal())
        create_variable(self, variable_name, literal)

    def extended_literal(self, ctx):
        if ctx.literal() != None:
            info = self.literal(ctx.literal())
        elif ctx.group() != None:
            info = self.group(ctx.group())
        return info

    def group(self, ctx):
        variables = get_group_variables(self, ctx.group2())
        return {"type": "GROUP", "variables": variables}

    def literal(self, ctx):
        if ctx.basic_literal() != None:
            info = self.basic_literal(ctx.basic_literal())
        elif ctx.terminal_definition() != None:
            info = self.terminal_definition(ctx.terminal_definition())
        return info

    def terminal_definition(self, ctx):
        id = self.identification(ctx.identification())
        info = self.basic_literal(ctx.basic_literal())
        return {**info, "id": id}

    def basic_literal(self, ctx):
        if ctx.identification() != None:
            id = self.identification(ctx.identification())
            check_variable_exits(self, id)
            return self.get_all_variables()[id]
        elif ctx.execution() != None:
            (function_name, registry) = self.execution(ctx.execution())
            exection_type = self.functions[function_name]["type"]
            return {"type": exection_type, "name": registry}
        elif ctx.String() != None:
            return {"type": "STRING"}
        elif ctx.Boolean() != None:
            return {"type": "BOOLEAN"}
        elif ctx.Number() != None:
            return {"type": "NUMBER"}

    def execution_function_name(self, ctx):
        return get_execution_data(self, ctx)

    def definition_function_name(self, ctx):
        check_global_function(self)
        (id, parameters) = self.definition_function_name2(ctx)
        parameters = list_params_to_dict(self, parameters)
        return (id, parameters)

    def definition_function_name2(self, ctx):
        return get_definition_data(self, ctx)

    def parameters(self, ctx):
        return get_parameters_data(self, ctx.parameters3())

    def defintion_parameter(self, ctx):
        variable_name = self.identification(ctx.identification())
        literal = self.extended_literal(ctx.extended_literal())
        return (variable_name, literal)
