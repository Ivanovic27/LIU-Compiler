from preloaded_data import (global_function, initial_functions, initial_scope)
from beautifultable import BeautifulTable
import yaml
from Memory import Memory


class Global:
    functions = initial_functions
    current_register = 0
    current_scope = initial_scope
    pending_jumps = []
    current_cuadruple = 0

    def get_variables(self):
        return self.functions[self.current_scope].variables

    def add_variable(self, variable_name, variable):
        self.get_variables()[variable_name] = variable

    def get_global_variables(self):
        return self.functions[global_function].variables

    def get_parameters(self):
        return self.functions[self.current_scope].parameters

    def get_all_variables(self):
        scope_variables = self.get_variables()
        params_variables = self.get_parameters()
        global_variables = self.get_global_variables()
        return {**global_variables, **params_variables, **scope_variables}

    def get_variable(self, variable_name):
        variables = self.get_all_variables()
        if variable_name in variables:
            return variables[variable_name]
        else:
            return None

    def get_current_function(self):
        return self.functions[self.current_scope]

    def add_memory(self, value):
        if self.current_scope == global_function:
            memory.global_data.append(value)
        else:
            memory.local_segment.append(value)

    def get_last_data(self):
        if self.current_scope == global_function:
            return memory.get_last_global()
        else:
            return memory.get_last_local()

    def add_continuous_quadruples(self, id, table):
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
        if len(table) == 0:
            registry = self.get_last_data()
            memory.add_quadruple(id, None, None, registry)
            self.add_memory(None)
        else:
            for row in table:
                registry = self.get_last_data()
                memory.add_quadruple(id, row.virtual_direction, None, registry)
                self.add_memory(None)
        return registry

    def print_quadruples(self):
        print("*************     CODE            ************")
        table = BeautifulTable()
        table.column_headers = ["cont", "operator",
                                "left", "right", "direction"]
        for index, quadruple in enumerate(memory.code_segment):
            table.append_row([memory.get_code_value(index), quadruple.operator.name, quadruple.left,
                              quadruple.right, quadruple.virtual_direction])
        print(table)

    def print_constants(self):
        print("*************     CONSTANTS       ************")
        table = BeautifulTable()
        table.column_headers = ["cont", "value"]
        for index, constant in enumerate(memory.constant_data):
            table.append_row([memory.get_constant_value(index), constant])
        print(table)

    def print_globals(self):
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

    def print_all_functions(self):
        print(yaml.dump(self.functions))

    def print_function(self, function_name):
        print(yaml.dump(self.functions[function_name]))

    def add_jump(self, offset=0):
        self.pending_jumps.append(len(memory.code_segment) + offset)


memory = Memory()
global_data = Global()
