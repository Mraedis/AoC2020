filepath = 'input5'

seatlist = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        line = line.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        seatlist.append(int(line, 2))
        line = fp.readline()

seatlist = sorted(seatlist)
seat = 0

for x in range(1, len(seatlist)-1):
    if ((seatlist[x] + seatlist[x+1] + seatlist[x-1]) / 3) % 1:
        seat += seatlist[x]
print(seat/2)
