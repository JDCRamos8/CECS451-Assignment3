import random
import numpy as np


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = 0
        self.coord = set()      # Coordinates of attacking queens
    
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def fitness(self):
        self.fit = 0        # Reset board's fitness to 0 to prevent accumulation
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.coord.update([(i, j) , (i + k , j)])       # Adds attacking pairs to coordinate list
                            self.fit += 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.coord.update([(i, j) , (i + k , j - k)])
                            self.fit += 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.coord.update([(i, j) , (i + k , j + k)])
                            self.fit += 1

    def show(self):
        print(np.matrix(self.map))
        print("Fitness: ",  self.fit)
        print("Attacking Pairs: ", self.coord)

    def flip(self, i, j):
        if self.map[i][j] == 0:
            self.map[i][j] = 1
        else:
            self.map[i][j] = 0

    def get_map(self):
        return self.map
    
    def get_fit(self):
        return self.fit

    def get_pairs(self):
        return self.coord
            
if __name__ == '__main__':
    test = Board(5)
    test.fitness()
    test.show()    