import re


matched_nums = []
matched_symbols = []


f = open('./input', 'r')

for index, line in enumerate(f):
    line = line.strip('\n')
    if (match_num := re.finditer(r'\d+', line)) is not None:
        for match in match_num:
            matched_nums.append((match, int(index)))

    if (match_symbol := re.finditer(r'\*', line)) is not None:
        for match in match_symbol:
            matched_symbols.append((match, int(index)))

sum = 0

for symbol_tuple in matched_symbols:
    symbol = symbol_tuple[0]
    line = symbol_tuple[1]
    gears = []
    for num_tuple in matched_nums:
        num = num_tuple[0]
        line_num = num_tuple[1]
        if line + 1 >= line_num >= line - 1:
            if num.end() >= symbol.start() >= num.start() - 1:
                gears.append(num.group(0))
    if len(gears) == 2:
        sum += int(gears[0]) * int(gears[1])

print(sum)
