from __future__ import annotations

import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


OP_TO_RPS = dict(zip('ABC', 'RPS'))
ME_TO_RPS = dict(zip('XYZ', 'RPS'))

SHAPE = {'R': 1, 'P': 2, 'S': 3}
OUTCOME = {
    'R': {'R': 3, 'P': 0, 'S': 6},
    'P': {'R': 6, 'P': 3, 'S': 0},
    'S': {'R': 0, 'P': 6, 'S': 3},
}


def solve(data: str) -> int:
    total = 0
    for op, me in map(str.split, data.splitlines()):
        op, me = OP_TO_RPS[op], ME_TO_RPS[me]

        total += SHAPE[me]
        total += OUTCOME[me][op]

    return total


assert solve("""\
A Y
B X
C Z
""") == 15

print(solve(INPUT_DATA))  # 12794
