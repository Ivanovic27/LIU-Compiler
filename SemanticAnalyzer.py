from semantic_logic import *
from LiuListener import LiuGrammarListener
from globals import (global_data as gl, memory)
from validations import *
from Group import Group


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
            return self.execution_function_name(ctx)
        elif ctx.if_execution() != None:
            return self.if_execution(ctx)
        elif ctx.iterate_execution() != None:
            return self.iterate_execution(ctx)
        else:
            return do_default_execution(self, ctx)

    def execution_function_name(self, ctx):
        return do_function_execution(self, ctx.execution_function_name())

    def if_execution(self, ctx):
        return do_if_execution(self, ctx.if_execution())

    def else_execution(self, ctx):
        return do_else_execution(self, ctx.else_execution())

    def iterate_execution(self, ctx):
        return do_iterate_execution(self, ctx.iterate_execution())

    def return_statement(self, ctx):
        if ctx.group() != None:
            return_literal = self.group(ctx.group())
        else:
            return_literal = self.basic_literal(ctx.basic_literal())
        memory.add_quadruple(
            "RETURN", return_literal.virtual_direction, None, None)
        current_function = gl.get_current_function()
        check_return_type(current_function, return_literal)

    def definition_function(self, ctx):
        initial_virtual_direction = memory.get_last_code()
        (function_name, parameters) = self.definition_function_name(
            ctx.definition_function_name())
        # Change scope inside of the new function
        gl.current_scope = function_name
        parameters = definition_function_parameters(self, ctx, parameters)
        create_function(self, ctx, function_name, parameters,
                        initial_virtual_direction)

    def definition_variable(self, ctx):
        variable_name = self.identification(ctx.identification())
        literal = self.extended_literal(ctx.extended_literal())
        create_variable(variable_name, literal)

    def extended_literal(self, ctx):
        if ctx.literal() != None:
            info = self.literal(ctx.literal())
        elif ctx.list1() != None:
            info = self.list1(ctx.list1())
        return info

    def list1(self, ctx):
        (first_direction, variables) = get_list_variables(self, ctx.list2())
        return Group("", "LIST", variables, first_direction)

    def group(self, ctx):
        variables = get_group_variables(self, ctx.group2())
        return Group("", "GROUP", variables)

    def literal(self, ctx):
        if ctx.basic_literal() != None:
            info = self.basic_literal(ctx.basic_literal())
        elif ctx.terminal_definition() != None:
            info = self.terminal_definition(ctx.terminal_definition())
        return info

    def terminal_definition(self, ctx):
        id = self.identification(ctx.identification())
        info = self.basic_literal(ctx.basic_literal())
        info.name = id
        return info

    def basic_literal(self, ctx):
        return create_literal(self, ctx)

    def definition_function_name(self, ctx):
        check_global_function()
        return get_definition_data(self, ctx)

    def parameters(self, ctx):
        return get_parameters_data(self, ctx.parameters3())

    def defintion_parameter(self, ctx):
        variable_name = self.identification(ctx.identification())
        literal = self.extended_literal(ctx.extended_literal())
        new_dir = gl.get_last_data()
        gl.add_memory(None)
        memory.add_assign(literal.virtual_direction, new_dir)
        return (variable_name, literal, new_dir)
