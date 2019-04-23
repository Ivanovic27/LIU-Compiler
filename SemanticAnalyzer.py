from semantic_logic import *
from LiuListener import LiuGrammarListener
from globals import (global_data as gl, memory)
from validations import *
from utils import list_params_to_dict
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
            (function_name, grps) = self.execution_function_name(
                ctx.execution_function_name())
            func = gl.functions[function_name]
            memory.code_segment.append(
                Cuadruple('ERA', func.virtual_directon, None, None))
            (new_function_name, groups) = do_execution(
                self, grps, function_name)
            parameters = gl.functions[function_name].parameters
            for group in groups:
                for key, parameter in parameters.items():
                    if parameter.pos == group.pos and parameter.param == group.param:
                        memory.code_segment.append(
                            Cuadruple('param', group.virtual_direction, None, parameter.virtual_direction))
            memory.code_segment.append(
                Cuadruple('gosub', func.code_direction, None, None))
            return (new_function_name, func.virtual_directon)
        elif ctx.if_execution() != None:
            return self.if_execution(ctx.if_execution())
        elif ctx.iterate_execution() != None:
            return self.iterate_execution(ctx.iterate_execution())
        else:
            return do_default_execution(self, ctx)

    def if_execution(self, ctx):
        do_if_execution(self, ctx)

    def else_execution(self, ctx):
        do_else_execution(self, ctx)

    def iterate_execution(self, ctx):
        do_iterate_execution(self, ctx)

    def return_statement(self, ctx):
        if ctx.group() != None:
            return_literal = self.group(ctx.group())
        else:
            return_literal = self.basic_literal(ctx.basic_literal())
        memory.code_segment.append(
            Cuadruple('RETURN', return_literal.virtual_direction, None, None))
        current_function = gl.get_current_function()
        check_return_type(current_function, return_literal)

    def definition_function(self, ctx):
        initial_virtual_direction = memory.get_last_code()
        (function_name, parameters) = self.definition_function_name(
            ctx.definition_function_name())
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
        variables = get_list_variables(self, ctx.list2())
        return Group("", "LIST", variables)

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

    def execution_function_name(self, ctx):
        return get_execution_data(self, ctx)

    def definition_function_name(self, ctx):
        check_global_function()
        (id, parameters) = get_definition_data(self, ctx)
        counter = 0
        for param in parameters:
            current_position = 0
            finish = False
            while not finish:
                found_item = False
                for (key, attr) in param.items():
                    if attr.pos == current_position:
                        attr.global_pos = counter
                        counter += 1
                        current_position += 1
                        found_item = True
                        break
                if not found_item:
                    finish = True
        parameters = list_params_to_dict(parameters)
        return (id, parameters)

    def parameters(self, ctx):
        return get_parameters_data(self, ctx.parameters3())

    def defintion_parameter(self, ctx):
        variable_name = self.identification(ctx.identification())
        literal = self.extended_literal(ctx.extended_literal())
        new_dir = memory.get_last_local()
        memory.local_segment.append(None)
        memory.add_assign(literal.virtual_direction, new_dir)
        return (variable_name, literal, new_dir)
