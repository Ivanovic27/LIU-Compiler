from semantic_logic import *
from LiuListener import LiuGrammarListener
import globals as gl
from validations import *
from utils import list_params_to_dict

class SemanticAnalyzer(LiuGrammarListener):
    def enterProgram(self, ctx):
        self.function_code(ctx.function_code())

    def identification(self, ctx):
        return get_id(ctx)

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
        current_function = gl.get_current_function()
        check_return_type(current_function, return_literal)

    def definition_function(self, ctx):
        (function_name, parameters) = self.definition_function_name(
            ctx.definition_function_name())
        create_function(self, ctx, function_name, parameters)

    def definition_variable(self, ctx):
        variable_name = self.identification(ctx.identification())
        literal = self.extended_literal(ctx.extended_literal())
        create_variable(variable_name, literal)

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
            check_variable_exits(id)
            return gl.get_all_variables()[id]
        elif ctx.execution() != None:
            (function_name, registry) = self.execution(ctx.execution())
            exection_type = gl.functions[function_name]["type"]
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
        check_global_function()
        (id, parameters) = get_definition_data(self, ctx)
        parameters = list_params_to_dict(parameters)
        return (id, parameters)

    def parameters(self, ctx):
        return get_parameters_data(self, ctx.parameters3())

    def defintion_parameter(self, ctx):
        variable_name = self.identification(ctx.identification())
        literal = self.extended_literal(ctx.extended_literal())
        return (variable_name, literal)
