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

        if not (r1_max < r2_min or r2_max < r1_min):
            total += 1

    return total


assert solve("""\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""") == 4

print(solve(INPUT_DATA))  # 837
