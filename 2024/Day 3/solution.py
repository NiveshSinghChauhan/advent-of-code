# https://adventofcode.com/2024/day/3

import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt") as file:
    input_string = file.read()

matches = re.finditer("(?<=mul\()\d+,\d+(?=\))", input_string, re.MULTILINE)

result = 0
for match in matches:
    num1, num2 = match.group().split(",")
    result += int(num1) * int(num2)

print(result)
