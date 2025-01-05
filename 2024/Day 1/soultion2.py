# https://adventofcode.com/2024/day/1

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

list_1 = []
list_2 = {}

with open(f"{dir_path}/input.txt") as file:
    for line in file:
        num_list_1, num_list_2 = line.split("   ")
        list_1.append(int(num_list_1))

        if int(num_list_2) in list_2:
            list_2[int(num_list_2)] += 1
        else:
            list_2[int(num_list_2)] = 1

result = 0
for num  in list_1:

    if num in list_2:
        result += num * list_2[num]

print(result)
