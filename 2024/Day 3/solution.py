# https://adventofcode.com/2024/day/3

import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt") as file:
    input_string = file.read()

matches = re.finditer(
    "(?<=mul\()\d+,\d+(?=\))|do\(\)|don't\(\)", input_string, re.MULTILINE
)

result = 0
should_multiply = True

for match in matches:

    instruction = match.group()

    if instruction == "do()":
        should_multiply = True
        continue
    elif instruction == "don't()":
        should_multiply = False
        continue

    if not should_multiply:
        continue

    num1, num2 = match.group().split(",")
    result += int(num1) * int(num2)

print(result)
