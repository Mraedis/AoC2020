arrival = 1000067
busses = '17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,439,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,787,' \
         'x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19'.split(',')
tbus = arrival - 1
for bus in busses:
    if bus != 'x':
        arrival - (arrival % int(bus)) + int(bus)
        if arrival - (arrival % int(bus)) + int(bus) < arrival - (arrival % tbus) + tbus:
            tbus = int(bus)
print(tbus * (tbus - (arrival % tbus)))
