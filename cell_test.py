import unittest
from cell import *

#Any live cell with fewer than two live neighbours dies, as if caused by under-population.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overcrowding.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_make_a_cell(self):
        uut = Cell(1,0)

        self.assertEqual(1, uut.x)

    def test_if_neighbor(self):
        uut = Cell(1,0)
        self.assertTrue(uut.is_neighbor(Cell(1,1)))

    def test_if_not_neighbor(self):
        uut = Cell(1,0)
        self.assertFalse(uut.is_neighbor(Cell(10,1)))

    def test_tree_neighbors(self):
        uut = Cell(1,0)
        cells = [Cell(10,0), Cell(1,1), Cell(0,0), Cell(2,0)]
        self.assertEqual(3, uut.neighbors(cells))

if __name__ == '__main__':
    unittest.main()
