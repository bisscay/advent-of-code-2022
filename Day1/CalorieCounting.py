#!/usr/bin/python3
"""Template.py
    Author: Bissallah Ekele - bAe
    Date: 04/12/2022
    Description: Elf with most food calorie stock.
"""
def get_calorie_stock(input_list):
    """Get list of each elf's calorie counts

        Keyword argument:
        input_list -- puzzle input 

        Return:
        Calorie stock list
    """
    calorie_count = 0
    calorie_stock = []

    for index, calorie in enumerate(input_list):
        if calorie:
            calorie_count += int(calorie)

        if not calorie or index == len(input_list) - 1:
            calorie_stock.append(calorie_count)
            calorie_count = 0

    return calorie_stock

def get_part_1(calorie_stock):
    """Get max calorie stock

        Keyword argument:
        calorie_stock -- list of elf calorie stock

        Return:
        Max calorie count
    """
    max_count = 0

    for calorie_count in calorie_stock:
        max_count = max(max_count, calorie_count)

    return max_count

def get_part_2(calorie_stock):
    """Get top 3 calorie stock

        Keyword argument:
        calorie_stock -- list of elf calorie stock

        Return:
        Sum of top 3 elf calorie stock
    """
    calorie_stock.sort()
    return (
        calorie_stock[-1]
        + calorie_stock[-2]
        + calorie_stock[-3]
    )

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = puzzle_input #test_input

    with open(file_name) as f:
        input_list = f.read().splitlines()

    calorie_stock = get_calorie_stock(input_list)

    print("Day_1 Part_1: " 
        + str(get_part_1(calorie_stock)) 
        + "\nPart_2: "
        + str(get_part_2(calorie_stock)))

if __name__ == "__main__":
    main()