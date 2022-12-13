from __future__ import annotations

import os
from collections import defaultdict

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


ALL_DIRS: defaultdict[str, dict[str, set[str]]]
ALL_FILES: dict[str, int]


def _calc_path(name: str, parent: str) -> str:
    if parent == '/':
        return f'/{name}'
    else:
        return f'{parent}/{name}'


def _register_dir(name: str, parent: str) -> str:
    path = _calc_path(name, parent)
    ALL_DIRS[parent]['dirs'].add(path)
    ALL_DIRS[path]
    return path


def _register_file(name: str, parent: str, size: int) -> str:
    path = _calc_path(name, parent)
    ALL_DIRS[parent]['files'].add(path)
    ALL_FILES[path] = size
    return path


def _calc_parent(path: str) -> str:
    if path.count('/') == 1:
        return '/'
    else:
        parent, _, _ = path.rpartition('/')
        return parent


def _calc_size(path: str) -> int:
    if (file_size := ALL_FILES.get(path)):
        return file_size

    dir_info = ALL_DIRS[path]
    return sum(_calc_size(child) for child in dir_info['dirs'] | dir_info['files'])


def solve(data: str) -> int:
    global ALL_DIRS, ALL_FILES
    ALL_DIRS = defaultdict(lambda: {'dirs': set(), 'files': set()})
    ALL_FILES = {}

    cwd = '/'
    for cmd_and_out in data[2:].split('\n$'):
        cmd, *out = cmd_and_out.strip().splitlines()
        match cmd.split():
            case ['cd', '/']:
                cwd = '/'
            case ['cd', '..']:
                cwd = _calc_parent(cwd)
            case ['cd', name]:
                cwd = _register_dir(name, cwd)
            case ['ls']:
                for line in out:
                    match line.split():
                        case ['dir', name]:
                            _register_dir(name, cwd)
                        case [size_s, name]:
                            _register_file(name, cwd, int(size_s))

    min_dir_size = _calc_size('/') - 40_000_000
    return min(
        dir_size
        for d in ALL_DIRS.keys()
        if (dir_size := _calc_size(d)) >= min_dir_size
    )


assert solve(
    """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""",
) == 24933642

print(solve(INPUT_DATA))  # 7991939
