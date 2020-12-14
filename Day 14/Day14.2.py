oplist = [[op for op in line.strip().split(' = ')] for line in open('input14').readlines()]


def apply_mask(val, msk):
    rval = ''
    for v, ms in zip('{:036b}'.format(int(val)), msk):
        rval += ms if ms in 'X1' else v
    return rval


memvals = {}
mask = ''
for op, value in oplist:
    if op == 'mask':
        mask = value
    else:
        alist = [apply_mask(op[op.index('[')+1:op.index(']')], mask)]
        xpos = alist[0].find('X')
        while xpos >= 0:
            acopy = []
            for adr in alist:
                acopy.append(adr.replace('X', '0', 1))
                acopy.append(adr.replace('X', '1', 1))
            alist = acopy
            xpos = alist[0].find('X')
        for address in alist:
            memvals[address] = int(value)

print(sum(memvals.values()))
