from Quadruple import Quadruple
from Operator import Operator


class Memory:
    global_data = []
    constant_data = []
    code_segment = []
    stack_segment = []
    local_segment = []

    def get_global_value(self, num):
        return num + 0

    def get_local_value(self, num):
        return num + 600

    def get_constant_value(self, num):
        return num + 200

    def get_code_value(self, num):
        return num + 400

    def get_last_global(self):
        return self.get_global_value(len(self.global_data))

    def get_last_local(self):
        return self.get_local_value(len(self.local_segment))

    def get_last_constant(self):
        return self.get_constant_value(len(self.constant_data))

    def get_last_code(self):
        return self.get_code_value(len(self.code_segment))

    def fill_jump(self, code_dir, offset=0):
        self.code_segment[code_dir].virtual_direction = self.get_last_code(
        ) + offset

    def add_quadruple(self, operator, left, right, direction):
        self.code_segment.append(
            Quadruple(operator, left, right, direction))

    def add_goto(self, code_dir):
        if code_dir != None:
            code_dir = self.get_code_value(code_dir)
        self.add_quadruple(Operator.GOTO, None, None, code_dir)

    def add_gotoFalse(self, condition_dir, code_dir=None):
        if code_dir != None:
            code_dir = self.get_code_value(code_dir)
        self.add_quadruple(Operator.GOTOF, condition_dir, None, code_dir)

    def add_gotoTrue(self, condition_dir, code_dir=None):
        if code_dir != None:
            code_dir = self.get_code_value(code_dir)
        self.add_quadruple(Operator.GOTOT, condition_dir, None, code_dir)

    def add_assign(self, value_dir, destination_dir):
        self.add_quadruple(Operator.ASSIGN, value_dir, None, destination_dir)

    def add_constant(self, value, type):
        if type == "BOOLEAN":
            if value == "True":
                self.constant_data.append(True)
            elif value == "False":
                self.constant_data.append(False)
        elif type == "STRING":
            self.constant_data.append(value[1:-1])
        elif type == "NUMBER":
            self.constant_data.append(float(value))
        elif type == "NUMBER":
            self.constant_data.append(value)
