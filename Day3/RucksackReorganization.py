#!/usr/bin/python3
"""Template.py
    Author: Bissallah Ekele - bAe
    Date: 06/12/2022
    Description: Reorganizing one item in each Rucksack.
"""
# Pseudocode:
# find common character in both halves
# derive priority

def get_common_item(rucksack):
    """Find common character in both halves

        Keyword argument:
        rucksack -- string of items in a rucksack

        Return:
        string symbol of common item
    """
    bound = len(rucksack)/2
    for item in rucksack[0:bound]:
        if item in set(rucksack[bound:]):
            return item

def get_priority(item):
    """Derive item priority

        Keyword argument:
        item -- common item string

        Return:
        int priority of item
    """
    if item.isupper():        
        return ord(item) - (ord("A") - 27)

    return ord(item) - (ord("a") - 1)
    

def get_part_1(input_list):
    """Sum of priorities of common items

        Keyword argument:
        input_list -- list of rucksack

        Return:
        Priority sum int
    """
    total = 0

    for rucksack in input_list:
        common_item = get_common_item(rucksack)
        total += get_priority(common_item)
    
    return total

def get_part_2(input_list):
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