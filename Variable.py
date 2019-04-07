class Variable():
    name = ""
    type = ""
    virtual_direction = None

    def __init__(self, name, type, virtual_direction=None):
        self.name = name
        self.type = type
        self.virtual_direction = virtual_direction
