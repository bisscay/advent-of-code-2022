#!/usr/bin/python3
"""TreetopTreehouse.py
    Author: Bissallah Ekele - bAe
    Date: 12/12/2022
    Description: Looking for enough tree cover to keep house hidden.
"""
# Pseudocode
# Pick an internal cell
# check-row
# check-column
# if either is true, tree is visible

def check(start_index, stop_index, grid_list, cell_index):
    for index in range(start_index, stop_index):
        # print(grid_list[index], grid_list[cell_index])
        if grid_list[index] >= grid_list[cell_index]:
            return False
    return True

def check_row(cell_x, grid_row):
    # check-left, check-right
    return (
        check(0, cell_x, grid_row, cell_x)
        or check(cell_x+1, len(grid_row), grid_row, cell_x)
    )

def check_column(cell_y, grid_column):
    # check-top, check-bottom
    return(
        check(0, cell_y, grid_column, cell_y)
        or check(cell_y+1, len(grid_column), grid_column, cell_y)
    )

def is_visible(cell_y, cell_x, grid):
    grid_column = [] # Itch - same thing created for each row
    for index in range(len(grid)):
        grid_column.append(grid[index][cell_x])

    return (
        check_row(cell_x, grid[cell_y])
        or check_column(cell_y, grid_column)
    )

def get_part_1(input_list):
    # All trees at edge are visible
    count = (len(input_list) + len(input_list[0])) * 2 - 4

    for y_index in range(1, len(input_list)-1):
        for x_index in range(1, len(input_list[y_index])-1):
            if is_visible(y_index, x_index, input_list):
                count += 1
        # print("next row")
    return count

def get_before(start_index, stop_index, grid_list, cell_index):
    # Get count before cell (left or top lookup)
    count = 0
    for index in range(start_index, stop_index):
        count += 1
        if grid_list[index] >= grid_list[cell_index]:
            count = 1
    return count

def get_after(start_index, stop_index, grid_list, cell_index):
    # Get count after cell (right or bottom lookup)
    count = 0
    for index in range(start_index, stop_index):
        count += 1
        if grid_list[index] >= grid_list[cell_index]:
            return count
    return count

def get_part_2(input_list):
    # Scenic score
    max_score = 0
    for y_index in range(1, len(input_list)-1):
        for x_index in range(1, len(input_list[y_index])-1):
            # left-distance
            left = get_before(0, x_index, input_list[y_index], x_index)
            # right-distance
            right = get_after(x_index+1, len(input_list[y_index]), input_list[y_index], x_index)
            
            # Derive scenic column parameters            
            grid_column = [] # Extract this creation
            for index in range(len(input_list)):
                grid_column.append(input_list[index][x_index])

            # top-distance
            top = get_before(0, y_index, grid_column, y_index)
            # bottom-distance
            bottom = get_after(y_index+1, len(grid_column), grid_column, y_index)

            max_score = max((top * left * right * bottom), max_score)
    return max_score

def main():
    test_input = r"test-input"
    puzzle_input = "puzzle-input"

    file_name = puzzle_input #test_input

    with open(file_name) as f:
        input_list = f.read().splitlines()

    print("Part_1: " 
        + str(get_part_1(input_list)) 
        + "\nPart_2: "
        + str(get_part_2(input_list)))

if __name__ == "__main__":
    main()