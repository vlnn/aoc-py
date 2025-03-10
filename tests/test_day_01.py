#!/usr/bin/env python3
from aoc_py.day_01 import day_01_1, day_01_2

test_data = [
    (3, 4, 2, 1, 3, 3),
    (4, 3, 5, 3, 9, 3),
]


def test_day_01_1(mocker):
    mocker.patch("aoc_py.day_01.parse_input", return_value=test_data)
    assert day_01_1() == 11


def test_day_01_2(mocker):
    mocker.patch("aoc_py.day_01.parse_input", return_value=test_data)
    assert day_01_2() == 31
