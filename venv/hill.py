from board import *

board = Board(5)
board.fitness()
board.show()

map = board.get_map()

def neighbors(rowNumber, columnNumber):
    return [[map[i][j] if i >= 0 and i < len(map) and j >= 0 and j < len(map[0]) else 0
             for j in range(columnNumber - 2, columnNumber + 1)]
            for i in range(rowNumber - 2, rowNumber + 1)]

def hill_climbing():
    return 0

def get_adjacents():
    return 0

next_queen = board.coord.pop()
print("Next queen: " + str(next_queen))
adjacents = neighbors(next_queen[1], next_queen[0])

print("Adjacent cells: \n" + str(np.matrix(adjacents)))