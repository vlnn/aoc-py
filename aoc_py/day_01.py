#!/usr/bin/env python3
# https://adventofcode.com/2024/day/1
from functools import reduce
from operator import sub
from typing import Tuple, List

from aoc_py.common import load_input_lines

current_day = 1
first_part = 1
second_part = 2


def split_pair(pair: str) -> Tuple[int, int]:
    """Split a single string pair into two integers."""
    first, second = pair.split()
    return int(first), int(second)


def parse_input(day, part):
    lines = load_input_lines(day, part)
    pairs = list([split_pair(line) for line in lines])
    col1, col2 = zip(*pairs)
    return [col1, col2]


def day_01_1():
    print("parse_input(1, 1)")
    print(parse_input(1, 1))
    col1, col2 = parse_input(1, 1)
    col1 = sorted(col1)
    col2 = sorted(col2)
    distances = list(map(lambda x, y: abs(y - x), col1, col2))
    total = sum(distances)
    return total


def day_01_2():
    col1, col2 = parse_input(1, 1)
    scores = list(map(lambda x: x * col2.count(x), col1))
    print(scores)
    total = sum(scores)
    return total


def main():
    print(day_01_1())
    print(day_01_2())


if __name__ == "__main__":
    main()
