oplist = [[op for op in line.strip().split(' = ')] for line in open('input14').readlines()]


def apply_mask(val, msk):
    rval = ''
    for v, ms in zip('{:036b}'.format(val), msk):
        rval += v if ms == 'X' else ms
    return int(rval, 2)


memvals = {}
mask = ''
for op, value in oplist:
    if op == 'mask':
        mask = value
    else:
        address = op[op.index('[')+1:op.index(']')]
        memvals[address] = apply_mask(int(value), mask)

print(sum(memvals.values()))
