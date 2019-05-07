from Quadruple import Quadruple
from Operator import Operator


class Memory:
    global_data = []
    constant_data = []
    code_segment = []
    stack_segment = []
    local_segment = []
    start_global = 0
    start_constant = 2000
    start_code = 4000
    start_local = 6000

    def get_global_value(self, num):
        """
        Name: get_global_value
        Description: Returns the virtual direction according to global memory
        Parameters: num: Index of global segment
        Returns: Virtual direction according to global values
        Important methods where its called:
        """
        return num + self.start_global

    def get_local_value(self, num):
        """
        Name: get_local_value
        Description: Returns the virtual direction according to local memory
        Parameters: num: Index of local segment
        Returns: Virtual direction according to local values
        Important methods where its called:
        """
        return num + self.start_local

    def get_constant_value(self, num):
        """
        Name: get_constant_value
        Description: Returns the virtual direction according to the constant memory
        Parameters: num: Index of constant segment
        Returns: Virtual direction according to constant values
        Important methods where its called:
        """
        return num + self.start_constant

    def get_code_value(self, num):
        """
        Name: get_code_value
        Description: Returns the virtual direction according to code memory
        Parameters: num: Index of code segment
        Returns: Virtual direction according to code values
        Important methods where its called:
        """
        return num + self.start_code

    def get_last_global(self):
        """
        Name: get_last_global
        Description: Returns the last virtual direction on the global memory
        Parameters: NA
        Returns: Last virtual direction on the global memory
        Important methods where its called:
        """
        return self.get_global_value(len(self.global_data))

    def get_last_local(self):
        """
        Name: get_last_local
        Description: Returns the last virtual direction on the local memory
        Parameters: NA
        Returns: Last virtual direction on the local memory
        Important methods where its called:
        """
        return self.get_local_value(len(self.local_segment))

    def get_last_constant(self):
        """
        Name: get_last_constant
        Description: Returns the last virtual direction on the constant memory
        Parameters: NA
        Returns: Last virtual direction on the constant memory
        Important methods where its called:
        """
        return self.get_constant_value(len(self.constant_data))

    def get_last_code(self):
        """
        Name: get_last_code
        Description: Returns the last virtual direction on the code memory
        Parameters: NA
        Returns: Last virtual direction on the code memory
        Important methods where its called:
        """
        return self.get_code_value(len(self.code_segment))

    def fill_jump(self, code_dir, offset=0):
        """
        Name: fill_jump
        Description: Fills a Goto Jump depending on a given direction and the last generated code memory created
        Parameters: NA
        Returns: NA
        Important methods where its called:
        """
        self.code_segment[code_dir].virtual_direction = self.get_last_code(
        ) + offset

    def add_quadruple(self, operator, left, right, direction):
        """
        Name: add_quadruple
        Description: Adds a quadruple to code segment memory
        Parameters:
            - operator: Operation to be added on quadruple
            - left: left value of quadruple
            - right: right value of quadruple
            - direciton: direction of result of quadruple
        Returns: NA
        Important methods where its called:
        """
        self.code_segment.append(
            Quadruple(operator, left, right, direction))

    def add_goto(self, code_dir):
        """
        Name: add_goto
        Description: Adds a  GOTO quadruple to code segment memory
        Parameters:
            - code_dire: Direction where GOTO must go
        Returns: NA
        Important methods where its called:
        """
        if code_dir != None:
            code_dir = self.get_code_value(code_dir)
        self.add_quadruple(Operator.GOTO, None, None, code_dir)

    def add_gotoFalse(self, condition_dir, code_dir=None):
        """
        Name: add_gotoFalse
        Description: Adds a  GOTOF quadruple to code segment memory
        Parameters:
            - condition_dir: Direction where the condition result is
            - code_dire: Direction where GOTO must go
        Returns: NA
        Important methods where its called:
        """
        if code_dir != None:
            code_dir = self.get_code_value(code_dir)
        self.add_quadruple(Operator.GOTOF, condition_dir, None, code_dir)

    def add_assign(self, value_dir, destination_dir):
        """
        Name: add_assign
        Description: Adds an ASSIGN quadruple to code segment memory
        Parameters:
            - value_dir: Direction where the value to assign is
            - destination_dir: Direction where the assignation must be applyed
        Returns: NA
        Important methods where its called:
        """
        self.add_quadruple(Operator.ASSIGN, value_dir, None, destination_dir)

    def add_constant(self, value, val_type):
        """
        Name: add_constant
        Description: Adds a constant to the data segment
        Parameters:
            - value: Value to be appended into the constant memory
            - val_type: Type of the value to be added as a constant
        Returns: NA
        Important methods where its called: used in many parts to create a constant with the right type.
        """
        if val_type == "BOOLEAN":
            if value == "True":
                self.constant_data.append(True)
            elif value == "False":
                self.constant_data.append(False)
        elif val_type == "STRING":
            self.constant_data.append(value[1:-1])
        elif val_type == "NUMBER":
            self.constant_data.append(float(value))
        elif val_type == "ANY":
            self.constant_data.append(value)
