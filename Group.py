from Variable import Variable


class Group(Variable):
    variables = []

    def __init__(self, name, type, variables, virtual_direction=None):
        self.variables = variables
        Variable.__init__(self, name, type, virtual_direction)
