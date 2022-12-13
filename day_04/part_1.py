from __future__ import annotations

import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    total = 0
    for pair in data.splitlines():
        r1, r2 = pair.split(',')
        r1_min, r1_max = map(int, r1.split('-'))
        r2_min, r2_max = map(int, r2.split('-'))

        if (
            (r1_min <= r2_min and r1_max >= r2_max) or
            (r2_min <= r1_min and r2_max >= r1_max)
        ):
            total += 1

    return total


assert solve("""\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""") == 2

print(solve(INPUT_DATA))  # 450
