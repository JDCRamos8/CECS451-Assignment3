from board import *
import random


# Given a state's map, return a string of encoded queen's coordinates
def encode_map(map):
    encoded_queens = ""

    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 1:
                encoded_queens += str(j + 1)

    return encoded_queens


# Given a string, return a map of decoded queen's coordinates
def decode_map(encoded):
    map = [[0 for column in range(0, 5)] for queen in range(0, 5)]

    column = 0
    for queen in encoded:
        map[column][int(queen) - 1] = 1
        column += 1

    return map


def genetic_algorithm():
    FIVE_CHOOSE_TWO = 10
    states = []
    h_values = []
    restarts = 0

    # Generate 8 states for five queens
    for i in range(8):
        states.append(Board(5))


    # Calculate fitness(h) for each state, 5C2 - Attacking Pairs
    for state in states:
        state.fitness()
        fitness = FIVE_CHOOSE_TWO - state.get_fit()
        h_values.append(fitness)


    while 10 not in h_values:       # Restart until solution state is in fitness values
        # SELECTION
        total = sum(h_values)

        h_normalize = []
        # Normalize fitness values
        for state in states:
            fitness = FIVE_CHOOSE_TWO - state.get_fit()
            normalization = round(fitness / total , 2)
            h_normalize.append(normalization)

        # Decimal values h where 0 <= h < 1
        h_ranges = []

        prev_h = 0
        for h in h_normalize:
            upper_bound = round(prev_h + h, 2)
            h_ranges.append(upper_bound)
            prev_h += round(h , 2)


        # Randomly select 8 states based on decimal value r (0, 1]
        selected_states = []
        for i in range(len(states)):
            r = round(random.random(), 2)

            if 0 <= r < h_ranges[0]:
                selected_states.append(states[0])
            elif h_ranges[0] <= r < h_ranges[1]:
                selected_states.append(states[1])
            elif h_ranges[1] <= r < h_ranges[2]:
                selected_states.append(states[2])
            elif h_ranges[2] <= r < h_ranges[3]:
                selected_states.append(states[3])
            elif h_ranges[3] <= r < h_ranges[4]:
                selected_states.append(states[4])
            elif h_ranges[4] <= r < h_ranges[4]:
                selected_states.append(states[5])
            elif h_ranges[5] <= r < h_ranges[5]:
                selected_states.append(states[6])
            else:
                selected_states.append(states[7])


        selection_strings = []
        for state in selected_states:       # Convert selected states into encoded strings
            selection_strings.append(encode_map(state.get_map()))


        # CROSSOVER
        crossover_strings = []
        # Create 4 pairs for 8 strings
        for string_one, string_two in zip(selection_strings[0::2], selection_strings[1::2]):
            r = random.randint(1, 4)        # Randomly choose index to split strings

            first_slice = (string_one[0:r], string_one[r:len(string_one)])
            second_slice = (string_two[0:r], string_two[r:len(string_two)])

            # Swap string halfs
            crossover_strings.append(first_slice[0] + second_slice[1])
            crossover_strings.append(second_slice[0] + first_slice[1])


        # MUTATION
        mutated_strings = []
        for cross_string in crossover_strings:
            rand_index = random.randint(0, 4)       # Generate index to change in string
            new_queen = random.randint(1, 5)        # Generate new queen (1-5) to change at random index

            if r < 5:       # Mutate string if 0 <= r <= 4
                mut_string = cross_string[0:rand_index] + str(new_queen) + cross_string[rand_index + 1:len(cross_string)]
                mutated_strings.append(mut_string)

            else:           # Keep crossover string
                mutated_strings.append(cross_string)


        h_values.clear()                                            # Clear 8 previous state fitnesses

        for state, mut_string in zip(states, mutated_strings):      # Recalculate heuristic for new strings
            new_map = decode_map(mut_string)
            state.map = new_map;

            state.fitness()
            fitness = FIVE_CHOOSE_TWO - state.get_fit()
            h_values.append(fitness)

        if 10 not in h_values:
            restarts += 1


    solution_index = h_values.index(10)
    solution_state = states[solution_index]

    return (solution_state, restarts)


def main():
    start_time = time.time() * 1000
    result = genetic_algorithm()
    end_time = time.time() * 1000

    elapsed_time = round(end_time - start_time)

    print("Running time: " + str(elapsed_time) + "ms")
    print("# of restart: " + str(result[1]))
    result[0].print_map()

main()
