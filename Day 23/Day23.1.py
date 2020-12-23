import collections as cl
inp = cl.deque([int(c) for c in '583976241'], 9)

cnt = 0
while cnt < 100:
    num = inp.popleft()
    tnum = ((num + 7) % 9) + 1
    target = inp.index(tnum)
    while target < 3:
        tnum = ((tnum + 7) % 9) + 1
        target = inp.index(tnum)
    move = [inp.popleft() for _ in range(3)]
    for x, m in enumerate(move):
        inp.insert(inp.index(tnum) + x + 1, m)
    inp.appendleft(num)
    inp.rotate(-1)
    cnt += 1

while inp.index(1) > 0:
    inp.append(inp.popleft())

prnt = ''
for i in inp:
    prnt += str(i)
print(prnt[1:])
