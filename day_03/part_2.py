from __future__ import annotations

import os
import string

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


PRIORITY = {ch: i for i, ch in enumerate(string.ascii_letters, 1)}


def solve(data: str) -> int:
    rucksacks = data.splitlines()

    total = 0
    for i in range(0, len(rucksacks), 3):
        common = (set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2])).pop()
        total += PRIORITY[common]

    return total


assert solve("""\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""") == 70

print(solve(INPUT_DATA))  # 2646
