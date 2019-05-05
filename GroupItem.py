class GroupItem():
    virtual_direction = None
    type = ""
    pos = None
    param = None

    def __init__(self, type, pos, virtual_direction=None, param=None, list_info=None):
        self.type = type
        self.pos = pos
        self.virtual_direction = virtual_direction
        self.param = param
        self.list_info = list_info
