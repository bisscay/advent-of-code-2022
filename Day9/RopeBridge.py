#!/usr/bin/python3
"""Template.py
    Author: Bissallah Ekele - bAe
    Date: 13/12/2022
    Description: 
"""
# Modeling rope physics - figure out where not to step
# Knot determines head and tail of rope
# Nebulous reasoning involving Plank Lengths
# Series of head motions - puzzle input
# Determine how tail will move
#
# H and T always touching, diagonally adjacent or overlapping
#  
# Pseudocode
# R, H -> y R
# T.check(H)
# if False, T.set_x(R-1)
# T.track((yR-1)) --> set.add()
# 
# U, H -> U x
# T.check(H)
# if False, T.set_y(U-1), T.set_u(x-1)
# T.track

def get_part_1(input_list):
    pass

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