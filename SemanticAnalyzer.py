from semantic_logic import *
from LiuListener import LiuGrammarListener
from globals import (global_data as gl, memory)
from validations import *
from Group import Group


class SemanticAnalyzer(LiuGrammarListener):
    """
    Name: SemanticAnalyzer
    Description: Has all the main rules used in antlr4 for semantic analysis.
    """

    def enterProgram(self, ctx):
        """
        Name: enterProgram
        Description: Walks through the generated tree strcuture from the first rule until the last one.
        Parameters:
            ctx: Holds the context of the root node.
        Returns: NA
        Important methods where its called: NA
        """
        self.function_code(ctx.function_code())
        memory.add_quadruple(Operator.EOF, None, None, None)

    def identification(self, ctx):
        """
        Name: identification
        Description: Gets the id from identification rule.
        Parameters:
            ctx: Holds the context of the identification rule.
        Returns: Returns the generated Id.
        Important methods where its called:
        Any method that requires the name of an identification (specially definitions and executions).
        """
        return get_id(ctx)

    def function(self, ctx):
        """
        Name: function
        Description: Compiles the code of the current function's scope.
        Parameters:
            ctx: Holds the context of the function rule.
        Returns: NA
        Important methods where its called:
        create_function, if executions (do_if_execution and do_else_execution) and iterate executions (do_iterate_execution).
        """
        self.function_code(ctx.function_code())

    def function_code(self, ctx):
        """
        Name: function_code
        Description: Compiles every line of the code of the current scope.
        Parameters:
            ctx: Holds the context of the function_code rule.
        Returns: NA
        Important methods where its called:
        enterProgram, function and itself.
        """
        if ctx.instruction() != None:
            self.instruction(ctx.instruction())
            self.function_code(ctx.function_code())

    def instruction(self, ctx):
        """
        Name: instruction
        Description: Compiles a line of code.
        Parameters:
            ctx: Holds the context of the instruction rule.
        Returns: NA
        Important methods where its called:
        function_code (to execute every line of code).
        """
        if ctx.definition() != None:
            self.definition(ctx.definition())
        elif ctx.execution() != None:
            self.execution(ctx.execution())
        elif ctx.return_statement() != None:
            self.return_statement(ctx.return_statement())

    def definition(self, ctx):
        """
        Name: definition
        Description: Compiles a definition (array, function or variable).
        Parameters:
            ctx: Holds the context of the definition rule.
        Returns: NA
        Important methods where its called:
        instruction (to execute a definition inside a scope).
        """
        if ctx.definition_function_name():
            self.definition_function(ctx)
        elif ctx.array_access():
            literal = self.basic_literal(ctx.basic_literal())
            (variable_name, registry) = self.array_access(ctx.array_access())
            memory.add_assign(literal.virtual_direction, registry)
        else:
            self.definition_variable(ctx)

    def array_access(self, ctx):
        """
        Name: array_access
        Description: Compiles an access to an array/matrix.
        Parameters:
            ctx: Holds the context of the array_access rule.
        Returns: Name of the array and its virtual direction in memory.
        Important methods where its called:
            create_literal: For the definition of literals.
            definition: To assign a value in the array index.
        """
        variable_name = self.identification(ctx.identification())
        items = self.array_access2(ctx.array_access2())
        check_variable_exits(variable_name)
        variable = gl.get_variable(variable_name)
        registry = None
        if variable != None:
            (size, i, _) = variable.array_info
            if len(items) > len(i):
                raise ValueError("The dimensions of array '" + variable_name + "' do not match.")
            previous_aux = None
            current_aux = None
            for (index, x) in enumerate(i):
                dir = items[index].virtual_direction
                current_aux = dir
                memory.add_quadruple(Operator.VER, dir, 0, x["size"] - 1)
                if index < len(i) - 1:
                    current_aux = gl.get_last_data()
                    memory.add_quadruple(
                        Operator.MULTIPLY, dir, x["m"], current_aux)
                    gl.add_memory(None)
                if index >= 1:
                    memory.add_quadruple(
                        Operator.SUM, previous_aux, current_aux, gl.get_last_data())
                    current_aux = gl.get_last_data()
                    gl.add_memory(None)
                previous_aux = current_aux
            memory.add_quadruple(Operator.SUM, current_aux,
                                 variable.constant_direction, gl.get_last_data())
            registry = gl.get_last_data()
            gl.add_memory(None)
        return (variable_name, '(' + str(registry) + ')')

    def array_access2(self, ctx):
        """
        Name: array_access2
        Description: Gets the array index for the function array access
        Parameters:
            ctx: Holds the context of the array_access2 rule.
        Returns: The inside the array access Ex: A[4,2,3] returns -> [4,2,3]
        Important methods where its called:
            array_access: Every time there's a definition or literal creation
        """
        items = []
        if ctx.basic_literal() != None:
            item = self.basic_literal(ctx.basic_literal())
            rest_items = self.array_access2(ctx.array_access3())
            items = [item] + rest_items
        return items

    def execution(self, ctx):
        """
        Name: execution
        Description: Executes if statements, functions or loops
        Parameters:
            ctx: Holds the context of the execution rule.
        Returns: Depending on the execution
            For:
                - Functions: Returns the name of the function 
                - If and loops: nothing
                - default execution: Function name and a virtual direction 
        Important methods where its called:
            array_access: Every time there's a definition or literal creation
        """
        if ctx.execution_function_name() != None:
            return self.execution_function_name(ctx)
        elif ctx.if_execution() != None:
            self.if_execution(ctx)
        elif ctx.iterate_execution() != None:
            self.iterate_execution(ctx)
        else:
            return do_default_execution(self, ctx)

    def execution_function_name(self, ctx):
        """
        Name: execution_function_name
        Description: Compiles a call to a user defined function.
        Parameters:
            ctx: Holds the context of the execution_function_name rule.
        Returns: The name of the function and its returned direction.
        Important methods where its called:
            execution: To execute a user definied function.
        """
        return do_function_execution(self, ctx.execution_function_name())

    def if_execution(self, ctx):
        """
        Name: if_execution
        Description: Compiles an if statement.
        Parameters:
            ctx: Holds the context of the execution rule.
        Returns: NA
        Important methods where its called:
            execution: To execute an if statement.
        """
        do_if_execution(self, ctx.if_execution())

    def else_execution(self, ctx):
        """
        Name: else_execution
        Description: Compiles an else statement.
        Parameters:
            ctx: Holds the context of the if_execution rule.
        Returns: NA
        Important methods where its called:
            do_if_execution: To execute an else statement.
        """
        return do_else_execution(self, ctx.else_execution())

    def iterate_execution(self, ctx):
        """
        Name: iterate_execution
        Description: Compiles a while iterate statement.
        Parameters:
            ctx: Holds the context of the execution rule.
        Returns: NA
        Important methods where its called:
            execution: To execute an iterate statement.
        """
        do_iterate_execution(self, ctx.iterate_execution())

    def return_statement(self, ctx):
        """
        Name: return_statement
        Description: Compiles the return statement.
        Parameters:
            ctx: Holds the context of the return_statement rule.
        Returns: NA
        Important methods where its called:
            instruction: To execute a return statement for the current scope.
        """
        return_literal = self.basic_literal(ctx.basic_literal())
        current_function = gl.get_current_function()
        memory.add_quadruple(
            Operator.RETURN, return_literal.virtual_direction, None, current_function.return_direction)
        check_return_type(current_function, return_literal)

    def definition_function(self, ctx):
        """
        Name: definition_function
        Description: Compiles the definition of a user defined function.
        Parameters:
            ctx: Holds the context of the definition rule.
        Returns: NA
        Important methods where its called:
            definition: To define a new user defined function.
        """
        memory.add_quadruple(Operator.STARTPROC, None, None, None)
        initial_virtual_direction = memory.get_last_code()
        literal = self.extended_literal(ctx.extended_literal())
        return_direction = memory.get_last_global()
        if literal.type == 'LIST':
            (size, _, _) = literal.array_info
            literal.virtual_direction = return_direction
            literal.constant_direction = memory.get_last_constant()
            memory.add_constant(return_direction, 'NUMBER')
            for _ in range(0, size):
                gl.add_memory(None)
        else:
            memory.global_data.append(None)
            memory.add_quadruple(
                Operator.ASSIGN, literal.virtual_direction, None, return_direction)
        (function_name, parameters) = self.definition_function_name(
            ctx.definition_function_name())
        # Change scope inside of the new function
        gl.current_scope = function_name
        parameters = definition_function_parameters(self, ctx, parameters)
        create_function(self, ctx, function_name, parameters,
                        initial_virtual_direction, literal, return_direction)

    def definition_variable(self, ctx):
        """
        Name: definition_variable
        Description: Creates a new variable or replaces its value in the current scope.
        Parameters:
            ctx: Holds the context of the definition rule.
        Returns: NA
        Important methods where its called:
            definition: To create a variable as a definition.
        """
        variable_name = self.identification(ctx.identification())
        literal = self.extended_literal(ctx.extended_literal())
        create_variable(variable_name, literal)

    def extended_literal(self, ctx):
        """
        Name: extended_literal
        Description: Gets info from a literal or array.
        Parameters:
            ctx: Holds the context of the extended_literal rule.
        Returns: Information about an extended literal.
        Important methods where its called:
            definition: To define a new extended literal
            definition_function: To get the literal from the default return function. 
            definition_parameters: To get the literal with the default value of the parameters.
        """
        literal = None
        if ctx.basic_literal() != None:
            literal = self.basic_literal(ctx.basic_literal())
        elif ctx.array() != None:
            literal = self.array(ctx.array())
        return literal

    def array(self, ctx):
        """
        Name: array
        Description: Gets info from an array.
        Parameters:
            ctx: Holds the context of the array rule.
        Returns: Information about an array.
        Important methods where its called:
            extended_literal: To get the information about the array literal.
        """
        item = int(ctx.Number().getText())
        rest_items = self.array_dimension(ctx.array_dimension())
        items = [item] + rest_items
        final_items = []
        size = 1
        for item in items:
            size = size * item
        temp = size
        new_dir = memory.get_last_constant()
        memory.constant_data.append(size)
        for item in items:
            temp = temp / item
            final_items.append({"m": memory.get_last_constant(), "size": item})
            memory.constant_data.append(temp)
        return Variable("", "LIST", None, (size, final_items, new_dir))

    def array_dimension(self, ctx):
        """
        Name: array_dimension
        Description: Gets the array dimensions that wants to be created.
        Parameters:
            ctx: Holds the context of the array_dimension.
        Returns: A list of size dimensions.
        Important methods where its called:
            array: To get the size of dimensions of an array declaration.
        """
        items = []
        if ctx.Number() != None:
            item = int(ctx.Number().getText())
            rest_items = self.array_dimension(ctx.array_dimension())
            items = [item] + rest_items
        return items

    def group(self, ctx):
        """
        Name: group
        Description: Compiles part of the parameters of a function call.
        Parameters:
            ctx: Holds the context of the group rule.
        Returns: NA
        Important methods where its called:
            prepare_arguments: To get part of the arguments of a function.
        """
        variables = get_group_variables(self, ctx.group2())
        return Group("", "GROUP", variables)

    def basic_literal(self, ctx):
        """
        Name: basic_literal
        Description: Gets the information of a created literal.
        Parameters:
            ctx: Holds the context of the basic_literal rule.
        Returns: Information about a basic literal (string, number, etc).
        Important methods where its called:
            extended_literal: To create and get the information of a literal.
            group: To create and get the information of a literal.
            array_access2: To create and get the information of a literal.
            return_statement:To create and get the information of a literal.
            get_group_variables: To create and get the information of a literal.
        """
        return create_literal(self, ctx)

    def definition_function_name(self, ctx):
        """
        Name: definition_function_name
        Description: Creates a new function.
        Parameters:
            ctx: Holds the context of the definition_function_name rule.
        Returns: The name of the function and its parameters info.
        Important methods where its called:
            definition: To create a new function.
        """
        check_global_function()
        return get_definition_data(self, ctx)

    def parameters(self, ctx):
        """
        Name: parameters
        Description: Gets all the parameters the group of a function.
        Parameters:
            ctx: Holds the context of the parameters rule.
        Returns: The name of the function and its parameters info of a group.
        Important methods where its called:
            definition_function_parameters: To access all the parameters of a function.
        """
        return get_parameters_data(self, ctx.parameters3())

    def defintion_parameter(self, ctx):
        """
        Name: defintion_parameter
        Description: Generates quadruples for parameters of a function with its default value.
        Parameters:
            ctx: Holds the context of the definition_function rule.
        Returns: NA
        Important methods where its called:
            get_parameters_data: To access information about a parameter.
        """
        variable_name = self.identification(ctx.identification())
        literal = self.extended_literal(ctx.extended_literal())
        new_dir = gl.get_last_data()
        gl.add_memory(None)
        if literal.type == 'LIST':
            new_dir = gl.get_last_data()
            literal.constant_direction = memory.get_last_constant()
            memory.add_constant(new_dir, 'NUMBER')
            (size, _, _) = literal.array_info
            for _ in range(0, size):
                gl.add_memory(None)
        else:
            memory.add_assign(literal.virtual_direction, new_dir)
        return (variable_name, literal, new_dir)
