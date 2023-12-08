import re

game_power = []

f = open('./input', 'r')

for line in f:
    line = line.strip('\n')
    if (game_id_re := re.search(r'Game (\d+):', line)) is not None:
        game_id = game_id_re.group(1)

        highest_blue = max(map(int, re.findall(r'(\d+) blue', line)))
        highest_red = max(map(int, re.findall(r'(\d+) red', line)))
        highest_green = max(map(int, re.findall(r'(\d+) green', line)))
        game_power.append(highest_blue * highest_red * highest_green)

sum = 0

for game in game_power:
    sum += int(game)


print(sum)
