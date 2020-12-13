from functools import reduce

bbusses = ['17,x,13,19', '67,7,59,61', '67,x,7,59,61', '67,7,x,59,61', '1789,37,47,1889',
           '17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,439,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,'
           '787,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19']


def chinese_remainder(n, a):
    sm = 0
    prod = reduce(lambda c, b: c * b, n)
    for n_i, c_i in zip(n, a):
        p = prod//n_i
        sm += c_i * mul_inv(p, n_i)*p
    return sm % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


for bb in bbusses:
    busses = bb.split(',')
    blist = {}
    for x, bus in enumerate(busses):
        if bus != 'x':
            blist[int(bus)] = (-x) % int(bus)
    print(chinese_remainder(blist.keys(), blist.values()))
