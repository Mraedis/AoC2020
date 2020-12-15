inp = [0, 14, 1, 3, 7, 9]

turns = {}
for x, num in enumerate(inp):
    turns[num] = x
last = inp[-1]

for i in range(len(turns.keys()), 30000000):
    nnum = 0 if last not in turns else i - 1 - turns[last]
    turns[last] = i - 1
    last = nnum
print(last)
