from copy import deepcopy

vector = {(1, -1, 0), (1, 0, 0), (1, 1, 0), (0, -1, 0), (0, 1, 0), (-1, -1, 0), (-1, 0, 0), (-1, 1, 0),
          (1, -1, 1), (1, 0, 1), (1, 1, 1), (0, -1, 1), (0, 1, 1), (-1, -1, 1), (-1, 0, 1), (-1, 1, 1),
          (1, -1, -1), (1, 0, -1), (1, 1, -1), (0, -1, -1), (0, 1, -1), (-1, -1, -1), (-1, 0, -1),
          (-1, 1, -1), (0, 0, 1), (0, 0, -1)}


def adjacent(height, row, col):
    adj = 0
    for z, x, y in vector:
        r, c, h = row + x, col + y, height + z
#        r = (row + x) % d if (row + x) >= d else abs(row + x) if (row + x) < 0 else (row + x)
#        c = (col + y) % d if (col + y) >= d else abs(col + y) if (col + y) < 0 else (col + y)
#        h = (height + z) % zr if (height + z) >= zr else abs(height + z) if (height + z) < 0 else (height + z)
        if 0 <= r < d and 0 <= c < d and 0 <= h < zr:
            if conway[h][r][c] == '#':
                adj += 1
    return adj


def updatemap(cw):
    newcw = deepcopy(cw)
    for z in range(zr):
        for x in range(d):
            for y in range(d):
                adj = adjacent(z, x, y)
                if cw[z][x][y] == '#':
                    newcw[z][x][y] = '#' if 1 < adj < 4 else '.'
                elif cw[z][x][y] == '.':
                    newcw[z][x][y] = '#' if adj == 3 else '.'
    return newcw


conwayf = [[c for c in line.strip()] for line in open('input17').readlines()]
d = 20
cy = 6
zr = 2*cy+1
inner = ['.'] * d
outer = []
conway = []
for _ in range(d):
    outer.append(inner.copy())
for _ in range(zr):
    conway.append(deepcopy(outer))


for w in range(cy, d - cy):
    conway[cy][w][cy:d - cy] = conwayf[w - cy]

for w in range(cy):
    alive = 0
    for matrix in conway:
        for rw in matrix:
            alive += rw.count('#')
    print(alive)
    conway = updatemap(conway)

alive = 0
for matrix in conway:
    for rw in matrix:
        alive += rw.count('#')
print(alive)
