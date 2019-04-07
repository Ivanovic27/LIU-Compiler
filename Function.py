class Function:
    name = ""
    type = ""
    variables = {}
    parameters = {}
    infiniteParams = False

    def __init__(self, name, type, variables, parameters, infiniteParams=False):
        self.name = name
        self.type = type
        self.variables = variables
        self.parameters = parameters
        self.infiniteParams = infiniteParams
