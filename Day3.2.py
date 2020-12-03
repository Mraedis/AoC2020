import math
import copy
filepath = 'input3'

steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
multi = 1

for stepx, stepy in steps:
    trees = 0
    treemap = []
    treemapex = []
    linel = 0
    lines = 0

    with open(filepath) as fp:
        line = fp.readline()
        linel = len(line)
        while line:
            lines += 1
            treemap.append(list(line[:-1]))
            line = fp.readline()

    treemapex = copy.deepcopy(treemap)

    for y in range(0, len(treemap)):
        for x in range(0, int(math.ceil(lines/linel * stepx/stepy))+1):
            treemapex[y].extend(treemap[y])

    for x in range(1, int(math.floor(lines / stepy))):
        if treemapex[stepy * x][stepx * x] == '#':
            trees += 1
    multi *= trees
print(multi)
