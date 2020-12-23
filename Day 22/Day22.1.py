import queue

inp = [line.rstrip('\n') for line in open('input22').read().split('\n\n')]
plyrs = {}
for i in inp:
    pl = i.split(':\n')[0]
    plyrs[pl] = queue.Queue(maxsize=50)
    for j in i.split('\n')[1:]:
        plyrs[pl].put(int(j))

while not any(plyrs[q].full() for q in plyrs.keys()):
    p1, p2 = [plyrs[q].get() for q in plyrs.keys()]

    if p1 > p2:
        plyrs['Player 1'].put(p1)
        plyrs['Player 1'].put(p2)
    else:
        plyrs['Player 2'].put(p2)
        plyrs['Player 2'].put(p1)

sumprod = 0
for q in plyrs.keys():
    while not plyrs[q].empty():
        sumprod += plyrs[q].qsize() * plyrs[q].get()
print(sumprod)
