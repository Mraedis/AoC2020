inp = [0, 14, 1, 3, 7, 9]

turns = dict((num, x) for x, num in enumerate(inp))
last = inp[-1]

for i in range(len(turns.keys()), 2020):
    nnum = 0 if last not in turns else i - 1 - turns[last]
    turns[last] = i - 1
    last = nnum
print(last)
