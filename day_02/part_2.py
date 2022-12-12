from __future__ import annotations

import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


OP_TO_RPS = dict(zip('ABC', 'RPS'))

SHAPE = {'R': 1, 'P': 2, 'S': 3}
OUTCOME = {
    'R': {'R': 3, 'P': 0, 'S': 6},
    'P': {'R': 6, 'P': 3, 'S': 0},
    'S': {'R': 0, 'P': 6, 'S': 3},
}

SCORES = dict(zip((0, 3, 6), 'XYZ'))
ROUND_TO_ME_RPS = {}
for me, inner in OUTCOME.items():
    for op, score in inner.items():
        ROUND_TO_ME_RPS[op, SCORES[score]] = me


def solve(data: str) -> int:
    total = 0
    for op, out in map(str.split, data.splitlines()):
        op = OP_TO_RPS[op]
        me = ROUND_TO_ME_RPS[op, out]

        total += SHAPE[me]
        total += OUTCOME[me][op]

    return total


assert solve("""\
A Y
B X
C Z
""") == 12

print(solve(INPUT_DATA))  # 14979
