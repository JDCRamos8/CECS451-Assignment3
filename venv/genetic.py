from board import *
import random


FIVE_CHOOSE_TWO = 10
states = []
h_values = []


# Given a state's map, return a string of encoded queen's coordinates
def encode_map(map):
    encoded_queens = ""

    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 1:
                encoded_queens += str(j + 1)

    return encoded_queens

# Given a string, return a map of decoded queen's coordinates
def decode_map(encoded): #12345
    map = [[0 for column in range(0, 5)] for queen in range(0, 5)]

    column = 0
    for queen in encoded:
        map[column][int(queen) - 1] = 1
        column += 1

    return map

# Generate 8 states for five queens
for i in range(8):
    states.append(Board(5))


# Print state, encode state, and calculate fitness(h)
state_number = 1
total = 0
for state in states:
    print("State " + str(state_number))
    state.print_map()

    print("Encoded State: " + encode_map(state.get_map()))
    state.fitness()

    print("Number of attacking pairs: " + str(state.get_fit()))
    fitness = FIVE_CHOOSE_TWO - state.get_fit()
    h_values.append(fitness)

    print("Fitness: " + str(fitness) + "\n")

    total += fitness

    state_number += 1


# Selection
print("Total: " + str(total))
print("Fitness values: " + str(h_values))

h_normalize = []
# Normalize fitness values
for state in states:
    fitness = FIVE_CHOOSE_TWO - state.get_fit()
    normalization = round(fitness / total , 2)
    h_normalize.append(normalization)
print("Normalization: " + str(h_normalize))

# Decimal values h where 0 <= h < 1
h_ranges = []

prev_h = 0
for h in h_normalize:
    upper_bound = round(prev_h + h, 2)
    h_ranges.append(upper_bound)
    prev_h += round(h , 2)

print("H Ranges: " + str(h_ranges))

# Randomly select 8 states
selected_states = []
for i in range(len(states)):
    r = round(random.random(), 2)
    print("Random value: " + str(r))

    if 0 <= r < h_ranges[0]:
        selected_states.append(states[0])
        print("Selected state 1")
    elif h_ranges[0] <= r < h_ranges[1]:
        selected_states.append(states[1])
        print("Selected state 2")
    elif h_ranges[1] <= r < h_ranges[2]:
        selected_states.append(states[2])
        print("Selected state 3")
    elif h_ranges[2] <= r < h_ranges[3]:
        selected_states.append(states[3])
        print("Selected state 4")
    elif h_ranges[3] <= r < h_ranges[4]:
        selected_states.append(states[4])
        print("Selected state 5")
    elif h_ranges[4] <= r < h_ranges[4]:
        selected_states.append(states[5])
        print("Selected state 6")
    elif h_ranges[5] <= r < h_ranges[5]:
        selected_states.append(states[6])
        print("Selected state 7")
    else:
        selected_states.append(states[7])
        print("Selected state 8")

selection_strings = []
for state in selected_states:
    selection_strings.append(encode_map(state.get_map()))

crossover_strings = []
# Create 4 pairs for 8 strings
for string_one, string_two in zip(selection_strings[0::2], selection_strings[1::2]):
    r = random.randint(1, 4)        # Randomly choose index to split strings

    first_slice = (string_one[0:r], string_one[r:len(string_one)])
    second_slice = (string_two[0:r], string_two[r:len(string_two)])

    # Swap string halfs
    crossover_strings.append(first_slice[0] + second_slice[1])
    crossover_strings.append(second_slice[0] + first_slice[1])

print("Selection strings:")
print(str(selection_strings))

print("Cross-over strings:")
print(str(crossover_strings))

# Mutation
mutated_strings = []
for cross_string in crossover_strings:
    r = random.randint(1, 5)
    if r < 5:       # Mutate string if 0 <= r <= 4
        print("Cross string: " + cross_string)
        print("Change queen " + str(r + 1))
        print("Change " + cross_string[r] + " to " + str(r))
        mut_string = cross_string[0:r] + str(r) + cross_string[r + 1:len(cross_string)]
        print(cross_string + " -> " + mut_string)
        mutated_strings.append(mut_string)
        print()
    else:
        mutated_strings.append(cross_string)

print("Mutated strings:")
print(str(mutated_strings))

h_values.clear()

for state, mut_string in zip(states, mutated_strings):
    new_map = decode_map(mut_string)
    state.map = new_map;
    state.fitness()
    fitness = FIVE_CHOOSE_TWO - state.get_fit()
    h_values.append(fitness)

print("New fitness values:")
print(h_values)