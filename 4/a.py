import re

f = open('./input', 'r')

sum = 0

for index, line in enumerate(f):
    line = line.strip('\n')
    line = re.split(r'Card.+\d+:', line)[1]
    split_line = line.split('|')
    match_count = 0

    winning_nums = re.findall(r'(\d+)', split_line[0])
    scratched_nums = re.findall(r'(\d+)', split_line[1])

    for num in winning_nums:
        if num in scratched_nums:
            match_count += 1

    if match_count > 0:
        points = 2 ** (match_count - 1)
        sum += points

print (sum)

