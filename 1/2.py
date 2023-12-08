
import re

values = []
numbers_dict = {
"zero": 'z0o',
"one": 'o1e',
"two": 't2o',
"three": 't3e',
"four": 'f4r',
"five": 'f5e',
"six": 's6x',
"seven": 's7n',
"eight": 'e8t',
"nine": 'n9e',
}

pattern = '|'.join(map(re.escape, numbers_dict.keys()))


with open('./1.input', 'r') as file:
    for line in file:
        line = line.strip('\n')
        old_line = line
        line = re.sub(pattern, lambda m: numbers_dict[m.group(0)], line)
        line = re.sub(pattern, lambda m: numbers_dict[m.group(0)], line)
        found_digits = list(map(int, re.findall(r'[0-9]', line)))
        if len(found_digits) != 0:
            values.append(int(str(found_digits[0]) + str(found_digits[-1])))
            print(old_line, line, found_digits, values[-1])

sum = 0
for value in values:
    sum = sum + value

print(sum)
