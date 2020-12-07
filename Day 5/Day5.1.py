filepath = 'input5'

seatlist = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        line = line.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        seatlist.append(int(line, 2))
        line = fp.readline()
print(sorted(seatlist)[-1])
