import math

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def is_neighbor(self, cell):
        dx = math.fabs(self.x - cell.x)
        dy = math.fabs(self.y - cell.y)

        return dx <= 1 and dy <= 1 and not (dx == dy == 0)

    def neighbors(self, cells):
        count = 0
        return sum(1 for cell in cells if self.is_neighbor(cell))
