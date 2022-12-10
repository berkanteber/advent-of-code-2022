from __future__ import annotations

import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    calories = [
        [int(x) for x in elf_data.splitlines()]
        for elf_data
        in data.split('\n\n')
    ]
    totals = [sum(elf_calories) for elf_calories in calories]

    return sum(sorted(totals, reverse=True)[:3])


assert solve("""\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""") == 45000

print(solve(INPUT_DATA))  # 200116
