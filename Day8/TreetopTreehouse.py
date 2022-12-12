#!/usr/bin/python3
"""Template.py
    Author: Bissallah Ekele - bAe
    Date: 12/12/2022
    Description: 
"""
# Enough tree cover to keep house hidden
# Looking along a row or column, visible trees
# 0 - 9 tree hight
# visible = shorter trees from edge to tree (horizontal/vertival look-up)
# All trees at edge are visible
# 
# Pseudocode
# Pick a cell
# check-left
# check-right
# check-top
# check-buttom
# if either is true, tree is visible

def check(start_index, stop_index, grid_list, cell_index):
    for index in range(start_index, stop_index):
        print(grid_list[index], grid_list[cell_index])
        if grid_list[index] >= grid_list[cell_index]:
            return False
    return True

def check_row(cell_x, grid_row):
    # check-left
    print(check(0, cell_x, grid_row, cell_x))
    
    # check-right
    # print(check(cell_x+1, len(grid_row), grid_row, cell_x))
    # for column in range(cell_x+1, len(grid_row)):
    return True


def is_visible(cell_y, cell_x, grid):
    return (
        check_row(cell_x, grid[cell_y])
    )

def get_part_1(input_list):
    # All trees at edge are visible
    count = (len(input_list) + len(input_list[0])) * 2 - 4

    for y_index in range(1, len(input_list)-1):
        for x_index in range(1, len(input_list[y_index])-1):
            if is_visible(y_index, x_index, input_list):
                count += 1
        print("next row")
    print(count)

def get_part_2(input_list):
    """Function description

        Keyword argument:
        input_list -- parameter description

        Return:
        returned value

        Throws:
        if exceptions are thrown
    """
    pass

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = test_input

    with open(file_name) as f:
        input_list = f.read().splitlines()

    print("Part_1: " 
        + str(get_part_1(input_list)) 
        + "\nPart_2: "
        + str(get_part_2(input_list)))

if __name__ == "__main__":
    main()