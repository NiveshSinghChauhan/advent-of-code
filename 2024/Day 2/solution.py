# https://adventofcode.com/2024/day/2

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def check_safe_level(levels: list[str]):

    cur = int(levels[0])
    next = int(levels[1])

    if (cur - next) == 0:
        return False

    dir = (cur - next) / abs(cur - next)

    for i in range(len(levels) - 1):
        cur = int(levels[i])
        next = int(levels[i + 1])

        diff = cur - next

        if abs(diff) == 0 or abs(diff) > 3:
            return False

        cur_dir = diff / abs(diff)

        if cur_dir != dir:
            return False

    return True


def check_after_one_rmv(line: list[str]):

    for i in range(len(line)):
        if check_safe_level(line[:i] + line[i + 1 :]):
            return True

    return False


with open(f"{dir_path}/input.txt") as file:

    safe_lvl_count = 0
    for line in file:
        if check_safe_level(line.split(" ")):
            safe_lvl_count += 1
        elif check_after_one_rmv(line.split(" ")):
            safe_lvl_count += 1

    print(safe_lvl_count)
