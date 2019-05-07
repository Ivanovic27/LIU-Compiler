class Quadruple:
    def __init__(self, operator, left, right, virtual_direction):
        """
        Name: Quadruple
        Description: Used to hold information of the quadruple.
        Parameters:
            operator: The operator to be used.
            left: The left part of the quadruple.
            right: The right part of the quadruple.
            virutal_direction: The direction where to hold the result.
        """
        self.operator = operator
        self.left = left
        self.right = right
        self.virtual_direction = virtual_direction
