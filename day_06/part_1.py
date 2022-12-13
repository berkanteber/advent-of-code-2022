from __future__ import annotations

import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    last4 = data[3] * 4
    for i, ch in enumerate(data, 1):
        last4 = last4[1:] + ch
        if len(set(last4)) == 4:
            return i

    raise AssertionError


assert solve('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
assert solve('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert solve('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert solve('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert solve('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

print(solve(INPUT_DATA))  # 1140
