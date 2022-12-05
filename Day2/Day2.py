#!/usr/bin/python3
"""Template.py
    Author: Bissallah Ekele - bAe
    Date: 05/12/2022
    Description: Rock Paper Scissors Tournament.
"""
# Pseudocode
# For each row
# Determin if it is a win, loss or draw
# Compute the score for the round

# Rules
# S > P -> 3 > 2
# P > R -> 2 > 1
# R > S -> 1 < 3
# # R = A = X
# # P = B = Y
# # S = C = Z
###
# 1 - Rock
# 2 - Paper
# 3 - Scissors
# Plus
# 0 - L
# 3 - D
# 6 - W

def get_winner(symbol_1, symbol_2):
    """Get winning choice

        Keyword argument:
        symbol -- string choice played

        Return:
        Wining choice string
    """
    if ((symbol_1 == "C" and symbol_2 == "Z") or
        (symbol_1 == "B" and symbol_2 == "Y") or
        (symbol_1 == "A" and symbol_2 == "X")
    ):
        return None

    if ((symbol_1 == "C" and symbol_2 == "Y") or
        (symbol_1 == "B" and symbol_2 == "X") or
        (symbol_1 == "A" and symbol_2 == "Z")
    ):
        return symbol_1

    return symbol_2

def get_play_weight(symbol):
    """Get weight of player's choice

        Keyword argument:
        symbol -- string choice played

        Return:
        Weight of choice int
    """
    if symbol in ["A", "X"]:
        return 1

    if symbol in ["B", "Y"]:
        return 2

    if symbol in ["C", "Z"]:
        return 3
    
    return 0

def get_score(oponent_choice, play):
    winner = get_winner(oponent_choice, play)
    play_weight = get_play_weight(play)
    # print(winner)
    # print(play_weight)

    if winner == None:
        return play_weight + 3
    
    if winner == play:
        return play_weight + 6
    
    # print(play_weight, score)

    return play_weight

def get_part_1(input_list):
    """Get score following strategy guide

        Keyword argument:
        input_list -- encrypted strategy guide

        Return:
        Score int
    """ 
    total = 0

    for round in input_list:
        total += get_score(round[0], round[-1])
            
    return total


def get_part_2(input_list):
    pass
    # score = 0

    # for round in input_list:
    #     play = get_play(round[0], round[-1])

    #     score += get_play_weight(round[0], play)
    
    # return score


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