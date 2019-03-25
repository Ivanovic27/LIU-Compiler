class Cuadruple:
    def __init__(self, operator, left, right, temporal):
        self.operator = operator
        self.left = left
        self.right = right
        self.temporal = temporal

    def __str__(self):
        return self.operator + ": " + self.left + ", " + self.right + " --> " + self.temporal
