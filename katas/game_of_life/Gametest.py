import unittest



# Cell: stayAlive()
class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Board(object):
    # size = 2
    # start: 0
    # end: size - 1
    def __init__(self):
        self.neighbours = 8


    # Finding all positions of the neighbours
    def findNeighbours(self, x, y):
        n = [
            Pos(x + 1, y),
            Pos(x,y+1),
            Pos(x + 1, y + 1),
            Pos(x - 1, y),
            Pos(x, y - 1),
            Pos(x - 1, y - 1),
            Pos(x - 1, y + 1),
            Pos(x + 1, y - 1)
        ]
        f = []
        for pos in n:
            x = pos.x
            y = pos.y
            if x >= 0 and y >= 0:
                f.append(pos)
        return f

class TestGameofLife(unittest.TestCase):

    board = Board()
    class Cell:

        def __init__(self):
            self.live = False
        def stayAlive(self, neighbours):
            live = 0
            for n in neighbours:
                if(n == 1): live +=1
            return live >= 2 and live <=3


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
        self.assertListEqual(sorted(self.board.findNeighbours(0,0)), sorted([Pos(0,1),Pos(1,1),Pos(1,0)]))

    def test_board_find_cell_neighbours_1_1(self):
        self.assertListEqual(sorted(self.board.findNeighbours(1,1)), sorted([(0,1),(0,0),(1,0)]))

# Board: matrix of cells
