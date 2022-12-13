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

class Knot:
    def __init__(self):
        self.x = self.y = 0

    def is_vertical(self, knot):
        return (
            abs(self.y - knot.y) <= 1 and
            self.x == knot.x
        )

    def is_horizontal(self, knot):
        return (
            abs(self.x - knot.x) <= 1 and
            self.y == knot.y
        )

    def is_diagonal(self, knot):
        return (
            abs(self.x - knot.x) <= 1 and
            abs(self.y - knot.y) <= 1
        )

    def move_x(self, steps):
        self.x += steps

    def move_y(self, steps):
        self.y += steps

def get_part_1(input_list):
    tail_cells = set()
    head = Knot()
    tail = Knot()
    
    print(head.x, head.y, tail.x, tail.y)
    for motion in input_list:
        direction, steps = motion.split(" ")
        steps = int(steps)
        
        if direction == "R":
            for step in range(1, steps+1):
                head.move_x(1)
                if not tail.is_horizontal(head) and not tail.is_diagonal(head):
                    if tail.y == head.y:
                        tail.move_x(1)
                    else:
                        tail.move_x(1)
                        if tail.y < head.y:
                            tail.move_y(1)
                        else:
                            tail.move_y(-1)
                tail_cells.add((tail.x,tail.y))
                print("R", step, "-->", head.x, head.y, tail.x, tail.y)

        if direction == "L":
            for step in range(1, steps+1):
                head.move_x(-1)
                if not tail.is_horizontal(head) and not tail.is_diagonal(head):
                    if tail.y == head.y:
                        tail.move_x(-1)
                    else:
                        tail.move_x(-1)
                        if tail.y < head.y:
                            tail.move_y(1)
                        else:
                            tail.move_y(-1)
                tail_cells.add((tail.x,tail.y))
                print("L", step, "-->", head.x, head.y, tail.x, tail.y)

        if direction == "U":
            for step in range(1, steps+1):
                head.move_y(1)
                if not tail.is_vertical(head) and not tail.is_diagonal(head):
                    if tail.x == head.x:
                        tail.move_y(1)
                    else:
                        tail.move_y(1)
                        if tail.x < head.x:
                            tail.move_x(1)
                        else:
                            tail.move_x(-1)
                tail_cells.add((tail.x,tail.y))
                print("U", step, "-->", head.x, head.y, tail.x, tail.y)

        if direction == "D":
            for step in range(1, steps+1):
                head.move_y(-1)
                if not tail.is_vertical(head) and not tail.is_diagonal(head):
                    if tail.x == head.x:
                        tail.move_y(-1)
                    else:
                        tail.move_y(-1)
                        if tail.x < head.x:
                            tail.move_x(1)
                        else:
                            tail.move_x(-1)
                tail_cells.add((tail.x,tail.y))
                print("D", step, "-->", head.x, head.y, tail.x, tail.y)
        
    print(tail_cells)
    return len(tail_cells)

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

    print("Part_1: " 
        + str(get_part_1(input_list)) 
        + "\nPart_2: "
        + str(get_part_2(input_list)))

if __name__ == "__main__":
    main()