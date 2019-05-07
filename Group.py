from Variable import Variable


class Group(Variable):

    def __init__(self, name, type, variables, virtual_direction=None, size=0):
        """
        Name: Group
        Description: Used to hold a group with several literals with information.
        """
        self.variables = variables
        self.size = size
        Variable.__init__(self, name, type, virtual_direction, None)
