import unittest


class TestGameofLife(unittest.TestCase):


    class Cell:

        def __init__(self):
            self.live = False
        def stayAlive(self, neighbours):
            live = 0
            for n in neighbours:
                if(n == 1): live +=1
            return live >= 2 and live <=3



    class Board:

        class Pos:
            def __init__(self, x, y):
                self.x = x
                self.y = y
        #size = 2
        # start: 0
        # end: size - 1
        def __init__(self):
            self.neighbours = 8

        # Finding all positions of the neighbours
        def findNeighbours(self, x, y):
            n = [
                self.Pos(x+1,y),
                self.Pos(x,y+1),
                self.Pos(x+1,y+1),
                (x-1,y),
                (x,y-1),
                (x-1,y-1),
                (x-1,y+1),
                (x+1,y-1)
            ]

            return n
    board = Board()
    c1 = Cell()
    def test_live_cell_dies_when_0_alive(self):
        self.assertEqual(self.c1.stayAlive([0, 0, 0]), False)

    def test_live_cell_dies_when_1_alive(self):
        self.assertEqual(self.c1.stayAlive([0, 0, 1]), False)

    def test_live_cell_alive_when_2_alive(self):
        self.assertEqual(self.c1.stayAlive([0, 1, 1]), True)

    def test_live_cell_alive_when_3_alive(self):
        self.assertEqual(self.c1.stayAlive([1, 1, 1]), True)

    def test_live_cell_dies_when_4_alive(self):
        self.assertEqual(self.c1.stayAlive([1, 1, 1, 1, 0, 0]), False)


    def test_board_find_cell_neighbours_0_0(self):
        self.assertEqual(self.board.findNeighbours(0,0), [(0,1),(1,1),(1,0)])

# Board: matrix of cells


# Cell: stayAlive()
