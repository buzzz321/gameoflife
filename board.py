from cell import *
#Any live cell with fewer than two live neighbours dies, as if caused by under-population.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overcrowding.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

class Board:

    def __init__(self, seed):
        self.cells = seed
        self.dead_cells = []

    
    def rule_1(self):
        """
        Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        """
        return [cell for cell in self.cells if cell.neighbors(self.cells) < 2]        

    def rule_2(self):
        """
        Any live cell with two or three live neighbours lives on to the next generation.

        """
        ret_val = []
        for cell in self.cells:
            neighbors = cell.neighbors(self.cells)
            if neighbors == 2 or neighbors == 3:
                ret_val.append(cell)
        return ret_val

