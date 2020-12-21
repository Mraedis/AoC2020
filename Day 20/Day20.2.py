from copy import deepcopy


def mirror(t, d):
    tmp = []
    if d == 'h':
        for j in range(len(t)):
            tmp.append(list(reversed(t[j])))
    else:
        tmp = deepcopy(t)
        for j in range(len(t)):
            tmp[j] = t[len(t) - 1 - j]
    return tmp


def rot(t):
    return list(map(list, zip(*t)))[::-1]


def isedge(t1, t2):
    if t1[0] == t2[-1]:
        return 'n'
    elif [i1[-1] for i1 in t1] == [i2[-1] for i2 in t2]:
        return 'e'
    elif t1[-1] == t2[0]:
        return 's'
    elif [i1[0] for i1 in t1] == [i2[0] for i2 in t2]:
        return 'w'
    else:
        return ''


inp = [line.rstrip('\n') for line in open('input20').read().split('\n\n')]
tiles = {}

for i in inp:
    title, tile = i.split('\n', 1)
    tiles[int(title.split(' ')[1][:-1])] = [[c for c in line] for line in tile.split('\n')]

tilemap = {}
for tile in tiles.keys():
    edges = {}
    for tx in tiles.keys():
        if tx == tile:
            continue
        tm = tiles[tx].copy()
        for x in range(4):
            match = isedge(tm, tiles[tile]) + isedge(tiles[tile], tm)
            if len(match):
                edges[match[0]] = tx
                continue
            tm = rot(tm)
        tm = mirror(tm, 'h')
        for x in range(4):
            match = isedge(tm, tiles[tile]) + isedge(tiles[tile], tm)
            if len(match):
                edges[match[0]] = tx
                continue
            tm = rot(tm)
        if len(edges) == 4:
            continue
    tilemap[tile] = edges

for t in tilemap[1949].values():
    print(tilemap[t])
