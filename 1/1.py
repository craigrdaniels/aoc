import re

values = []

with open('./1.input', 'r') as file:
    for line in file:
        line = line.strip('\n')
        found_digits = list(map(int, re.findall(r'[0-9]', line)))
        if len(found_digits) != 0:
            values.append(int(str(found_digits[0]) + str(found_digits[-1])))


sum = 0
for value in values:
    sum = sum + value

print(sum)
