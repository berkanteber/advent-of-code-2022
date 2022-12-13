from __future__ import annotations

import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> str:
    start, rearrange = data.split('\n\n')

    *levels, nums = start.splitlines()

    num_stacks = int(nums.split()[-1])
    stacks: list[list[str]] = [[] for _ in range(num_stacks)]
    for level in levels[::-1]:
        level = level.ljust(num_stacks*4, ' ')
        for i in range(num_stacks):
            if (ch := level[4*i + 1]) != ' ':
                stacks[i].append(ch)

    for inst in rearrange.splitlines():
        cnt, src, dst = map(int, inst.split()[1::2])
        for _ in range(cnt):
            item = stacks[src-1].pop()
            stacks[dst-1].append(item)

    return ''.join(stack.pop() for stack in stacks)


assert solve("""\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""") == 'CMZ'

print(solve(INPUT_DATA))  # FWNSHLDNZ
