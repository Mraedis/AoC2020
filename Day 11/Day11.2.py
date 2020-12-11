from copy import deepcopy

vector = {(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)}


def adjacent(row, col):
    adj = 0
    for x, y in vector:
        r, c = row + x, col + y
        while (valid := (0 <= r < rowl and 0 <= c < coll)) and seatmap[r][c] == '.':
            r, c = r + x, c + y
        if valid and seatmap[r][c] == '#':
            adj += 1
    return adj


def updateseats(sm):
    newmap = deepcopy(sm)
    for x in range(0, rowl):
        for y in range(0, coll):
            adj = adjacent(x, y)
            if sm[x][y] == 'L':
                newmap[x][y] = '#' if not adj else 'L'
            elif sm[x][y] == '#':
                newmap[x][y] = 'L' if adj > 4 else '#'
    return newmap


seatmap = [[c for c in line.strip()] for line in open('input11').readlines()]
rowl = len(seatmap)
coll = len(seatmap[0])

lastoccupied = 9999
occupied = 0

while lastoccupied != occupied:
    lastoccupied = occupied
    occupied = 0
    seatmap = updateseats(seatmap)
    for smrow in seatmap:
        occupied += smrow.count('#')
print(occupied)
