class GroupItem():
    virtual_direction = None
    type = ""
    pos = None
    param = None

    def __init__(self, type, pos, virtual_direction=None, param=None, array_info=None):
        self.type = type
        self.pos = pos
        self.virtual_direction = virtual_direction
        self.param = param
        self.array_info = array_info
