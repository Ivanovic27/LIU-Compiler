from Variable import Variable


class Group(Variable):
    variables = []

    def __init__(self, name, type, variables, virtual_direction=None, size=0):
        self.variables = variables
        self.size = size
        Variable.__init__(self, name, type, virtual_direction, None)
