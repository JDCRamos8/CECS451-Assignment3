from board import *
import copy

curr_state = Board(5)      # 5x5 Chess Board
curr_state.fitness()
curr_state.show()

map = curr_state.get_map()

def hill_climbing():
    return 0

def get_adjacents():
    return 0

next_queen = curr_state.coord.pop()
print("Next queen: " + str(next_queen))

# Get all coordinates in a row whose cell is 0 in the chosen queen's row
adjacents = []

for i in range(5):
    row = []
    if (curr_state.get_map()[next_queen[0]][i] == 0):
        row.append((next_queen[0] , i))
    adjacents.append(row)

print()
states = [(curr_state.get_map(), curr_state.get_fit())]
print(states)
print()

curr_state.flip(next_queen[0], next_queen[1])       # Flip previous queen to 0

print("CURRENT STATE AFTER FLIP")
curr_state.show()

cand_state = copy.deepcopy(curr_state)

print()
print("Adjacents: " + str(adjacents))
print()

for row in adjacents:
    state_number = 1
    for cell in row:
        next_state = copy.deepcopy(cand_state)
        next_state.flip(cell[0], cell[1])

        print("State " + str(state_number))
        next_state.fitness()
        next_state.show()
        print()

        # Record board & fitness
        states.append((next_state.get_map(), next_state.get_fit()))

        state_number += 1

states.sort(key = lambda fitness: fitness[1], reverse = True)

for map, fitness in states:
    print(map, fitness)