from preloaded_data import (global_function, initial_functions, initial_scope)
from beautifultable import BeautifulTable
import yaml
from Memory import Memory


class Global:
    """
    Name: Global
    Description: Contains common functions and global information for compilation.
    """
    # Contains all the functions, common and user defined.
    functions = initial_functions
    # The current function being accessed.
    current_scope = initial_scope
    # All the jumps that are pending in a stack.
    pending_jumps = []

    def get_variables(self):
        """
        Name: get_variables
        Description: Gets variables of the current function.
        Returns: The variables of a function.
        Important methods where its called:
            get_all_variables: To get variables of the function.
        """
        return self.functions[self.current_scope].variables

    def add_variable(self, variable_name, variable):
        """
        Name: add_variable
        Description: Adds a new variable to the current function.
        Parameters:
            variable_name: the name of the new variable to add.
            variable: The content of the variable to add.
        Returns: NA
        Important methods where its called:
            create_variable: To add it to the created variables.
        """
        self.get_variables()[variable_name] = variable

    def get_global_variables(self):
        """
        Name: get_global_variables
        Description: Gets global variables.
        Returns: The global variables.
        Important methods where its called:
            get_all_variables: To get the global variables.
        """
        return self.functions[global_function].variables

    def get_parameters(self):
        """
        Name: get_parameters
        Description: Gets global variables.
        Returns: The global variables.
        Important methods where its called:
            get_all_variables: To get the global variables.
        """
        return self.functions[self.current_scope].parameters

    def get_all_variables(self):
        """
        Name: get_all_variables
        Description: Gets all the variables considering parameters, globals and locals.
        Returns: All the variables.
        Important methods where its called:
            used in many parts of validations to check information of all variables.
        """
        scope_variables = self.get_variables()
        params_variables = self.get_parameters()
        global_variables = self.get_global_variables()
        return {**global_variables, **params_variables, **scope_variables}

    def get_variable(self, variable_name):
        """
        Name: get_variable
        Description: Gets the information of a variable (if it exists).
        Parameters:
            variable_name: The name of the variable to retrieve information.
        Returns: The variable or None if it does not exist.
        """
        variables = self.get_all_variables()
        if variable_name in variables:
            return variables[variable_name]
        else:
            return None

    def get_current_function(self):
        """
        Name: get_current_function
        Description: Gets the information of the current accessed function.
        Returns: Information about the function.
        Important methods where its called:
            return_statement: To check get the type of the function.
        """
        return self.functions[self.current_scope]

    def add_memory(self, value):
        """
        Name: add_memory
        Description: Adds memory to global or local, depending on the current scope.
        Parameters:
            value: The value to add to memory.
        Returns: NA
        Important methods where its called:
            many places use it to add memory when creating quadruples.
        """
        if self.current_scope == global_function:
            memory.global_data.append(value)
        else:
            memory.local_segment.append(value)

    def get_last_data(self):
        """
        Name: get_last_data
        Description: Gets the last memory added (global or local) depending on the current scope.
        Returns: The last memory.
        Important methods where its called:
            many places use it to access the last direction.
        """
        if self.current_scope == global_function:
            return memory.get_last_global()
        else:
            return memory.get_last_local()

    def add_continuous_quadruples(self, id, table):
        """
        Name: add_continuous_quadruples
        Description: Generates various quadruples with left and right directions.
        It is used for operations.
        Returns: The last direction used.
        Important methods where its called:
            types semantic_logic uses it for executions with multiple operations involved.
        """
        if len(table) == 0:
            registry = self.get_last_data()
            memory.add_quadruple(id, None, None, registry)
            temp = registry
            self.add_memory(None)
        else:
            temp = table[0].virtual_direction
            if len(table) == 1:
                registry = self.get_last_data()
                memory.add_quadruple(id, temp, None, registry)
                temp = registry
                self.add_memory(None)
            for row in table[1:]:
                registry = self.get_last_data()
                memory.add_quadruple(id, temp, row.virtual_direction, registry)
                temp = registry
                self.add_memory(None)
        return temp

    def add_left_quadruples(self, id, table):
        """
        Name: add_left_quadruples
        Description: Generates quadruples with only left directions.
        Returns: NA.
        Important methods where its called:
            types semantic_logic uses it for executions that use only left part (such as print).
        """
        if len(table) == 0:
            memory.add_quadruple(id, None, None, None)
        else:
            for row in table:
                memory.add_quadruple(id, row.virtual_direction, None, None)
        return None

    def add_array_quadruple(self, id, table):
        """
        Name: add_array_quadruple
        Description: Generates quadruples for arrays.
        Returns: The last direction.
        Important methods where its called:
            types semantic_logic uses it for executions that use arrays.
        """
        for row in table:
            (_, _, size_dir) = row.array_info
            registry = self.get_last_data()
            memory.add_quadruple(
                id, row.virtual_direction, size_dir, registry)
            self.add_memory(None)
        return registry

    def add_map_quadruple(self, id, group):
        """
        Name: add_map_quadruple
        Description: Generates quadruples for special functions with arrays.
        Returns: NA
        Important methods where its called:
            types semantic_logic uses it for executions that use special functions with arrays.
        """
        (_, _, size_dir) = group[0].array_info
        memory.add_quadruple(
            id, group[0].virtual_direction, size_dir, None)
        memory.add_quadruple(
            id, group[1].virtual_direction, group[2].virtual_direction, None)

    def print_quadruples(self):
        """
        Name: print_quadruples
        Description: Prints all the generated quadruples.
        Returns: NA
        Important methods where its called:
            main: To check the generated quadruples when it is finish compiling.
        """
        print("*************     CODE            ************")
        table = BeautifulTable()
        table.column_headers = ["cont", "operator",
                                "left", "right", "direction"]
        for index, quadruple in enumerate(memory.code_segment):
            table.append_row([memory.get_code_value(index), quadruple.operator.name, quadruple.left,
                              quadruple.right, quadruple.virtual_direction])
        print(table)

    def print_constants(self):
        """
        Name: print_constants
        Description: Prints all the list of constants.
        Returns: NA
        Important methods where its called:
            main: To check the constants when it is finish compiling.
        """
        print("*************     CONSTANTS       ************")
        table = BeautifulTable()
        table.column_headers = ["cont", "value"]
        for index, constant in enumerate(memory.constant_data):
            table.append_row([memory.get_constant_value(index), constant])
        print(table)

    def print_globals(self):
        """
        Name: print_globals
        Description: Prints all the list of globals.
        Returns: NA
        Important methods where its called:
            main: To check the constants when it is finish compiling.
        """
        print("*************     GLOBALS         ************")
        table = BeautifulTable()
        table.column_headers = ["cont", "name", "value"]
        for index, global_data in enumerate(memory.global_data):
            variable = [x for (key, x) in self.get_all_variables().items()
                        if x.virtual_direction == memory.get_global_value(index)]
            if len(variable) == 1:
                variable = variable[0].name
            else:
                variable = "(temp)"
            table.append_row([memory.get_global_value(
                index), variable, global_data])
        print(table)

    def print_function(self, function_name):
        """
        Name: print_all_functions
        Description: Prints a particular function.
        Parameters:
            function_name: The name of the function to print its information.
        Returns: NA
        Important methods where its called:
            main: To check the information inside a particular function.
        """
        print(yaml.dump(self.functions[function_name]))

    def add_jump(self, offset=0):
        """
        Name: add_jump
        Description: Adds a pending jump direction to the list.
        Parameters:
            offset: The direction for the jump to store.
        Returns: NA
        Important methods where its called:
            all if-else/iterate execution use it to store it to the pending jumps.
        """
        self.pending_jumps.append(len(memory.code_segment) + offset)


memory = Memory()
global_data = Global()
