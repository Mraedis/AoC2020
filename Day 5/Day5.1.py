filepath = 'input5'


def bin_to_dec(num):
    dec = 0
    for n in num:
        dec = dec * 2 + int(n)
    return dec


seatlist = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        line = line.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        seatlist.append(bin_to_dec(line))
        line = fp.readline()
print(sorted(seatlist)[-1])
