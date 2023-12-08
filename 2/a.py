import re

max_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14,
}

valid_games = []

f = open('./input', 'r')

for line in f:
    line = line.strip('\n')
    if (game_id_re := re.search(r'Game (\d+):', line)) is not None:
        game_id = game_id_re.group(1)

        highest_blue = max(map(int, re.findall(r'(\d+) blue', line)))
        highest_red = max(map(int, re.findall(r'(\d+) red', line)))
        highest_green = max(map(int, re.findall(r'(\d+) green', line)))
        if int(highest_blue) <= max_cubes['blue'] and int(highest_red) <= max_cubes['red'] and int(highest_green) <= max_cubes['green']:
            valid_games.append(game_id)

sum = 0

for game in valid_games:
    sum += int(game)


print(sum)
