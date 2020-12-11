from copy import deepcopy


def updateseats(sm):
    newmap = deepcopy(sm)
    for x in range(1, len(sm)-1):
        for y in range(1, len(sm[0])-1):
            adj = [sm[x+1][y-1], sm[x+1][y], sm[x+1][y+1], sm[x][y-1], sm[x][y+1],
                   sm[x-1][y-1], sm[x-1][y], sm[x-1][y+1]].count('#')
            if sm[x][y] == 'L':
                newmap[x][y] = '#' if not adj else 'L'
            elif sm[x][y] == '#':
                newmap[x][y] = 'L' if adj > 3 else '#'
    return newmap


smmid = [['.'] + [c for c in line.strip()] + ['.'] for line in open('input11').readlines()]
smtb = ['.'] * len(smmid[0])
seatmap = [smtb.copy()] + smmid + [smtb]

lastoccupied = 9999
occupied = 0

while lastoccupied != occupied:
    lastoccupied = occupied
    occupied = 0
    seatmap = updateseats(seatmap)
    for row in seatmap:
        occupied += row.count('#')
print(occupied)
