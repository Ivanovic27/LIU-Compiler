from Variable import Variable


class Group(Variable):
    variables = []

    def __init__(self, name, type, variables):
        self.variables = variables
        Variable.__init__(self, name, type)
