from copy import deepcopy

vector = set()
for dx in (-1, 0, 1):
    for dy in (-1, 0, 1):
        for dz in (-1, 0, 1):
            for dq in (-1, 0, 1):
                if dx == dy == dz == dq == 0:
                    continue
                else:
                    vector.add((dx, dy, dz, dq))


def adjacent(height, time, row, col):
    adj = 0
    for z, q, x, y in vector:
        r, c, h, t = row + x, col + y, height + z, time + q
        if 0 <= r < d and 0 <= c < d and 0 <= h < zr and 0 <= t < d:
            if conway[h][t][r][c] == '#':
                adj += 1
    return adj


def updatemap(cw):
    newcw = deepcopy(cw)
    for z in range(zr):
        for q in range(d):
            for x in range(d):
                for y in range(d):
                    adj = adjacent(z, q, x, y)
                    if cw[z][q][x][y] == '#':
                        newcw[z][q][x][y] = '#' if 1 < adj < 4 else '.'
                    elif cw[z][q][x][y] == '.':
                        newcw[z][q][x][y] = '#' if adj == 3 else '.'
    return newcw


conwayf = [[c for c in line.strip()] for line in open('input17').readlines()]
d = 20
cy = 6
zr = 2*cy+1
inner = ['.'] * d
middle = []
outer = []
conway = []
for _ in range(d):
    middle.append(deepcopy(inner))
for _ in range(d):
    outer.append(deepcopy(middle))
for _ in range(zr):
    conway.append(deepcopy(outer))

for w in range(cy, d - cy):
    conway[cy][w][cy][cy:d - cy] = conwayf[w - cy]

for w in range(cy):
    alive = 0
    for cube in conway:
        for matrix in cube:
            for rw in matrix:
                alive += rw.count('#')
    print(alive)
    conway = updatemap(conway)

alive = 0
for cube in conway:
    for matrix in cube:
        for rw in matrix:
            alive += rw.count('#')
print(alive)
