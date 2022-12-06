#!/usr/bin/python3
"""CampCleanup.py
    Author: Bissallah Ekele - bAe
    Date: 06/12/2022
    Description: Duplicate Camp Cleanup Jobs.
"""

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
        

def is_overlap(section_a, section_b):
    """One-way check if section is overlapping another

        Keyword argument:
        section_a -- first comparing section string
        section_b -- second comparing section string

        Return:
        boolean truth
    """
    split_a = section_a.split("-")
    split_b = section_b.split("-")
    return (
        (
            int(split_b[0]) >= int(split_a[0])
            and int(split_b[0]) <= int(split_a[-1])
        )
        or (
            int(split_b[-1]) >= int(split_a[0])
            and int(split_b[-1]) <= int(split_a[-1])
        )
    )

def get_part_2(input_list):
    """Get count of partially contained pair overlaps

        Keyword argument:
        input_list -- list of section pairs

        Return:
        int count of partially contained overlaps
    """
    count = 0

    for pair in input_list:
        split_pair = pair.split(",")
        if (
            is_overlap(split_pair[0], split_pair[-1])
            or is_overlap(split_pair[-1], split_pair[0]) # second way check
        ):
            count += 1
    
    return count

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