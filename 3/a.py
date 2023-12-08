import re

matched_nums = []
matched_symbols = []


f = open('./input', 'r')

for index, line in enumerate(f):
    line = line.strip('\n')
    if (match_num := re.finditer(r'\d+', line)) is not None:
        for match in match_num:
            matched_nums.append((match, int(index)))

    if (match_symbol := re.finditer(r'[^.\d]', line)) is not None:
        for match in match_symbol:
            matched_symbols.append((match, int(index)))

sum = 0
    
for matched_tuple in matched_nums:
    match = matched_tuple[0]
    line = matched_tuple[1]
    for matched_sym_tuple in matched_symbols:
        match_sym = matched_sym_tuple[0]
        line_sym = matched_sym_tuple[1]
        if line + 1 >= line_sym >= line - 1:
            if match.end() >= match_sym.start() >= match.start() - 1:
                sum += int(match.group(0))
    
print(sum)
