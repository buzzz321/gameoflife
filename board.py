from cell import *
#lint:disable
#Any live cell with fewer than two live neighbours dies, as if caused by under-population.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overcrowding.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
#lint:enable


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

    def rule_3(self):
        """
        Any live cell with more than three live neighbours dies, as if by overcrowding.

        """
        return [cell for cell in self.cells if cell.neighbors(self.cells) > 3]

    def rule_4(self, dead_cells, still_alive_cells):
        """
        Any live cell with more than three live neighbours dies, as if by overcrowding.

        """
        revived_cells = []
        for dead_cell in dead_cells:
            if dead_cell.neighbors(still_alive_cells) == 3:
                revived_cells.append(dead_cell)
                
        return revived_cells



