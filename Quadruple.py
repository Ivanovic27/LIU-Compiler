class Quadruple:
    operator = ''
    left = None
    right = None
    virtual_direction = None

    def __init__(self, operator, left, right, virtual_direction):
        self.operator = operator
        self.left = left
        self.right = right
        self.virtual_direction = virtual_direction
