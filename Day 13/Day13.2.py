bbusses = ['17,x,13,19', '67,7,59,61', '67,x,7,59,61', '67,7,x,59,61', '1789,37,47,1889',
           '17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,439,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,'
           '787,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19']


for bb in bbusses:
    busses = bb.split(',')
    blist = {}

    factor = 1
    for x, bus in enumerate(busses):
        if bus != 'x':
            bus = int(bus)
            factor *= bus
            blist[bus] = (-x) % bus

    target = 0
    for bus in blist.keys():
        quot = factor // bus
        target += blist[bus] * quot * pow(quot, bus - 2, bus)
        target %= factor
    print(target)
