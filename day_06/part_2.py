from __future__ import annotations

import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    last14 = data[13] * 14
    for i, ch in enumerate(data, 1):
        last14 = last14[1:] + ch
        if len(set(last14)) == 14:
            return i

    raise AssertionError


assert solve('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
assert solve('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
assert solve('nppdvjthqldpwncqszvftbrmjlhg') == 23
assert solve('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
assert solve('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26

print(solve(INPUT_DATA))  # 3495
