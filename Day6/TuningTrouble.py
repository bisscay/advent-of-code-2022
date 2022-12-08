#!/usr/bin/python3
"""TuningTrouble.py
    Author: Bissallah Ekele - bAe
    Date: 08/12/2022
    Description: Fix Faulty Communication System.
"""
# Add a subroutine -
# Lock on to another elve's signal to communicate
#
# Start of packet marker in datastream
# 1st position - four different characters
# 
# Pseudocode:
# place fours in a set - watch memory use
# if set size is four - return index at upper bound

def get_marker(datastream, window):
    """Get start-of marker

        Keyword argument:
        datastream -- elve's position datastream string
        window -- int sliding window to consider

        Return:
        start-of marker int
    """
    packet_match = set()
    for lower_bound in range(len(datastream)):
        packet_match.update(datastream[lower_bound:window+lower_bound])
        if len(packet_match) == window:
            return lower_bound + window
        packet_match.clear()
        

def get_part_1(input_list):
    """Get start-of-packet marker

        Keyword argument:
        input_list -- elve's position datastream list

        Return:
        start-of-packet marker int
    """
    for datastream in input_list:
        print(get_marker(datastream, 4))

def get_part_2(input_list):
    """Get start-of-message marker

        Keyword argument:
        input_list -- elve's position datastream list

        Return:
        start-of-message marker int
    """
    for datastream in input_list:
        print(get_marker(datastream, 14))

def main():
    test_input = r"test-input"
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