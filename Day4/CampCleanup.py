#!/usr/bin/python3
"""Template.py
    Author: Bissallah Ekele - bAe
    Date: 06/12/2022
    Description: 
"""
# Pseudocode
# 
# Check if pair-a bound is within pair-b
# Check if pair-b bound is within pair-a

def is_subset(superset, subset):
    """Check if one is a subset of the other

        Keyword argument:
        superset -- superset string
        subset -- subset string

        Return:
        boolean truth
    """
    split_superset = superset.split("-")
    split_subset = subset.split("-")
    return (
        int(split_superset[0]) <= int(split_subset[0])
        and int(split_superset[-1]) >= int(split_subset[-1])
    )

def get_part_1(input_list):
    """Get count of fully contained pair overlaps

        Keyword argument:
        input_list -- list of pairs

        Return:
        int count of fully contained overlaps
    """
    count = 0

    for pair in input_list:
        split_pair = pair.split(",")
        if (
            is_subset(split_pair[0], split_pair[-1])
            or is_subset(split_pair[-1], split_pair[0])
        ):
            count += 1
    
    return count
        

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

    file_name = puzzle_input #test_input

    with open(file_name) as f:
        input_list = f.read().splitlines()

    print("Day_1 Part_1: " 
        + str(get_part_1(input_list)) 
        + "\nPart_2: "
        + str(get_part_2(input_list)))

if __name__ == "__main__":
    main()