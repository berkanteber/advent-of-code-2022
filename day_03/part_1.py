from __future__ import annotations

import os
import string

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


PRIORITY = {ch: i for i, ch in enumerate(string.ascii_letters, 1)}


def solve(data: str) -> int:
    total = 0
    for rucksack in data.splitlines():
        mid = len(rucksack) // 2
        first, second = rucksack[:mid], rucksack[mid:]

        common = (set(first) & set(second)).pop()

        total += PRIORITY[common]

    return total


assert solve("""\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""") == 157

print(solve(INPUT_DATA))  # 7446
