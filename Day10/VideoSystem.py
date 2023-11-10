#!/usr/bin/python3
"""Cathode Ray Tube.py
    Author: Bissallah Ekele - bAe
    Date: 08/11/2023
    Description: Fix/replace the comm's video system.
"""

def compute_signal_strength(count, register_x):
    if count + 1 == 20:
        return 20 * register_x

    if count + 1 > 20 and ((count + 1) - 20) % 40 == 0:
        return (count + 1) * register_x

    return 0


def get_part_1(input_list):
    """Function description

        Keyword argument:
        input_list -- parameter description

        Return:
        returned value

        Throws:
        if exceptions are thrown
    """
    count = 0
    register_x = 1
    signal_strength = 0
    for instruction in input_list:
        if instruction[0] == "n":
            signal_strength += compute_signal_strength(count, register_x)
            count += 1

        if instruction[0] == "a":          
            cycle = 2
            while(cycle):
                signal_strength += compute_signal_strength(count, register_x)
                count += 1

                cycle -= 1
            
            v = int(instruction.split(" ")[-1])
            register_x += v
    
    return signal_strength

def get_screen():
    pixel_state =  {}
    for pixel in range(0, 240):
        pixel_state[pixel] = "."
    return pixel_state

def get_column_index(count):
    while count > 39:
        count -= 40
    return count

def is_match(count, register_x):
    sprite = [register_x - 1, register_x, register_x + 1]
    if count in sprite:
        return True
    return False

def update_screen(count, register_x, screen):                                
    column_index = get_column_index(count)

    if is_match(column_index, register_x):
        screen[count] = "#"

def display_row(screen, start, end):
    row = []
    for pixel in range(start, end):
        row.append(screen[pixel])
    
    display = []
    display.append("".join(row))
    print(display)

def display_screen(screen):
    row_count = 6
    start = 0
    end = 40
    while(row_count):
        display_row(screen, start, end)
        start += 40
        end += 40

        row_count -= 1

def get_part_2(input_list):
    screen = get_screen()

    count = 0
    register_x = 1
    for instruction in input_list:
        if instruction[0] == "n":
            update_screen(count, register_x, screen)
            count += 1

        if instruction[0] == "a":            
            cycle = 2
            while(cycle):
                update_screen(count, register_x, screen)
                count += 1

                cycle -= 1

            v = int(instruction.split(" ")[-1])
            register_x += v
            
    display_screen(screen)

def main():
    test_input = "test-input"
    puzzle_input = "puzzle-input"

    file_name = puzzle_input #test_input

    with open(file_name) as f:
        input_list = f.read().splitlines()

    print("Part_1: " 
        + str(get_part_1(input_list)) 
        + "\nPart_2: ")
    get_part_2(input_list)

if __name__ == "__main__":
    main()
    # FZBPBFZF