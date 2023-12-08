import re

f = open('./input', 'r')

copied_cards = {}
## (card, count)

sum = 0


for index, line in enumerate(f):
    line = line.strip('\n')
    current_card = 0
    if (match := re.search(r'(\d+):', line)) is not None:
        current_card = int(match.group(1))
    line = re.split(r'Card.+\d+:', line)[1]
    split_line = line.split('|')
    match_count = 0

    winning_nums = re.findall(r'(\d+)', split_line[0])
    scratched_nums = re.findall(r'(\d+)', split_line[1])

    for num in winning_nums:
        if num in scratched_nums:
            match_count += 1

    if match_count > 0:
        num_loops = 1
        if current_card in copied_cards:
            num_loops += copied_cards[current_card]
        for loop in range(num_loops):
            for i in range(current_card + 1, current_card + match_count + 1):
                if i in copied_cards:
                    copied_cards[i] += 1
                else:
                    copied_cards[i] = 1

    if current_card not in copied_cards:
        copied_cards[current_card] = 1
    else:
        copied_cards[current_card] += 1

for card in copied_cards:
    sum += copied_cards[card]

print(sum)
