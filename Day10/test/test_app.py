"""test_app.py
    Pytest module for AOC Day 10.
    Author: Bissallah Ekele - bAe
    Date: 08/11/2023
"""
import VideoSystem

test_sample = ["noop", "addx 3", "addx -5"]

class TestPart1():
    def test_sample(self):
        assert len(test_sample) == 3
        assert VideoSystem.get_part_1(test_sample) == 0
        assert VideoSystem.compute_signal_strength(20, 3) == 0
        assert VideoSystem.compute_signal_strength(19, 2) == 40
        assert VideoSystem.compute_signal_strength(21, 2) == 0
        assert VideoSystem.compute_signal_strength(80, 2) == 0
        assert VideoSystem.compute_signal_strength(79, 2) == 0
        assert VideoSystem.compute_signal_strength(39, 2) == 0
        assert VideoSystem.compute_signal_strength(59, 2) == 120

    def test_input(self):
        file_name = r".\test\test_input.txt"
        with open(file_name) as f:
            input_list = f.read().splitlines()
            assert len(input_list) == 146
            assert VideoSystem.get_part_1(input_list) == 13140
    