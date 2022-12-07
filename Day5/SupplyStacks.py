#!/usr/bin/python3
"""SupplyStacks.py
    Author: Bissallah Ekele - bAe
    Date: 07/12/2022
    Description: 
"""
# Pseudocode
# represent crates in stack as multi array
# modify multi-array based on move
# pick top characters in multi-array

def get_steps_start(input_list):
    # determine the point where crane procedure starts
    for index, entry in enumerate(input_list):
        if entry == "":
            return index + 1
    return -1 

def make_stacks(crates):
    # Trim out unwanted symbols and build n x m matrix
    for index, row in enumerate(crates):
        new_row = []
        count = 0
        for symbol in row:
            if symbol in [" ", "[", "]"]:
                count += 1
            if count == 4:
                new_row.append("")
                count = 0
            if symbol not in [" ", "[", "]"] and count >= 0:
                new_row.append(symbol)
                count = 0
        crates[index] = new_row
    return crates

def get_index_y(matrix, column):
    # Get first crate in a column
    for index in range(len(matrix)):
        if matrix[index][column] != "":
            return index

def move(matrix, amount, position_one, position_two, reverse_order=False):
    # Move crates following procedure 
    from_x = position_one - 1
    to_x = position_two - 1
    
    while (amount != 0):
        # pop
        from_y = get_index_y(matrix, from_x)

        if reverse_order:
            from_y = from_y + amount - 1

        crate = matrix[from_y][from_x]
        # print(crate)
        matrix[from_y][from_x] = ""
        
        # push
        to_y = get_index_y(matrix, to_x)
        if to_y == 0:
            matrix.insert(0, [""] * len(matrix[0]))
            matrix[to_y][to_x] = crate
        if to_y != 0:
            matrix[to_y-1][to_x] = crate

        amount -= 1

    return matrix

def get_part_1(input_list, reverse_order=False):
    # Find top crates following CrateMover 9000 procedure
    top_crates = []

    steps_start = get_steps_start(input_list)

    if steps_start == -1:
        print("No crane procedure")

    stacks = make_stacks(input_list[:steps_start-1])
    # print(stacks)
    steps = input_list[steps_start:]
    for step in steps:
        split_step = step.split(" ")

        if reverse_order:
            stacks = move(
                stacks,
                int(split_step[1]),
                int(split_step[3]),
                int(split_step[5]),
                True
            )
        else:
            stacks = move(
                stacks,
                int(split_step[1]),
                int(split_step[3]),
                int(split_step[5])
            )
        # print(stacks)
    
    for column_index in range(len(stacks[0])):
        row_index = get_index_y(stacks, column_index)
        top_crates.append(stacks[row_index][column_index])

    return "".join(top_crates)        

def get_part_2(input_list):
    # Find top crates following new CrateMover 9001 procedure
    return get_part_1(input_list, True)

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = puzzle_input #test_input

    with open(file_name) as f:
        input_list = f.read().splitlines()

    print("Day_1 Part_1: " 
        + str(get_part_1(input_list)) 
        + "\nPart_2: "
        + str(get_part_2(input_list)))

if __name__ == "__main__":
    main()