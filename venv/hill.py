from board import *
import copy
import time


def hill_climbing():
    curr_state = Board(5)  # 5x5 chess board
    curr_state.fitness()

    heuristic_cost = curr_state.get_fit()

    restart_condition = 0               # If result heuristic gets stuck 10 times, restart
    restarts = 0

    while heuristic_cost != 0:           # Continue while heuristic cost is not 0
        if restart_condition == 10:
            curr_state = Board(5)       # Create new random 5x5 chess board
            curr_state.fitness()

            restarts += 1
            restart_condition = 0

        next_queen = curr_state.coord.pop()     # Get coordinates of a random attacking queen

        adjacents = get_adjacents(curr_state, next_queen)

        states = [(curr_state.get_map(), curr_state.get_fit())]     # Record initial state & fitness

        cand_state = copy.deepcopy(curr_state)
        cand_state.flip(next_queen[0], next_queen[1])               # Flip previous queen to 0

        for row in adjacents:       # Generate a new state for each adjacent cell in row
            for cell in row:
                next_state = copy.deepcopy(cand_state)
                next_state.flip(cell[0], cell[1])

                next_state.fitness()

                states.append((next_state.get_map(), next_state.get_fit()))     # Record board & fitness

        states.sort(key=lambda fitness: fitness[1], reverse=True)       # Sort candidate states by fitness

        lowest_state = states.pop()

        if curr_state.get_fit() == lowest_state[1]:     # Prevents stuck at local minima
            restart_condition += 1

        heuristic_cost = lowest_state[1]        # Choose lowest heuristic cost of all candidates states
        curr_state.map = lowest_state[0]        # Assign lowest heuristic cost's map to current state
        curr_state.fitness()

    return (curr_state, restarts)


# Prints chess board where queens are "1" and everything else is "-"
def print_map(map):
    new_map = []

    for i in range(len(map)):
        row = []
        for j in range(len(map)):
            if map[i][j] == 1:
                row.append(str(map[i][j]))
            else:
                row.append("-")
        new_map.append(row)

    for row in new_map:
        print(" ".join(row))


# Given a current state and the (x, y) of next queen,
# Gets all coordinates in a row whose cell is 0 in the chosen queen's row
def get_adjacents(curr_state, next_queen):
    adjacents = []

    for i in range(5):
        row = []
        if (curr_state.get_map()[next_queen[0]][i] == 0):
            row.append((next_queen[0], i))
        else:
            continue
        adjacents.append(row)
    return adjacents

def main():
    start_time = time.time() * 1000
    result = hill_climbing()
    end_time = time.time() * 1000

    elapsed_time = round(end_time - start_time)

    print("Running time: " + str(elapsed_time) + "ms")
    print("# of restart: " + str(result[1]))
    print_map(result[0].map)

main()
