# https://adventofcode.com/2024/day/1

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

list_1 = []
list_2 = []

with open(f"{dir_path}/input.txt") as file:
    for line in file:
        num_list_1, num_list_2 = line.split("   ")
        list_1.append(int(num_list_1))
        list_2.append(int(num_list_2))

list_1.sort()
list_2.sort()

result = sum([abs(a - b) for a, b in zip(list_1, list_2)])

print(result)
