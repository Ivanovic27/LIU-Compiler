class Function:
    name = ""
    type = ""
    variables = {}
    parameters = {}
    infiniteParams = False
    virtual_directon = None
    return_direction = None
    code_direction = None

    def __init__(self, name, type, variables, parameters, infiniteParams=False, virtual_directon=None, code_direction=None, return_direction=None):
        self.name = name
        self.type = type
        self.variables = variables
        self.parameters = parameters
        self.infiniteParams = infiniteParams
        self.virtual_directon = virtual_directon
        self.code_direction = code_direction
        self.return_direction = return_direction
