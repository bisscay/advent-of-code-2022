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

def is_visible(cell, grid):
    pass
def get_part_1(input_list):
    for row in input_list:
        print(row)

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