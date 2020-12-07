import math

steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
multi = 1

for stepx, stepy in steps:
    trees = 0
    treemapex = []

    treemap = [[c for c in val.strip()] for val in open('input3').readlines()]
    linel = len(treemap[0])

    for x in range(1, int(math.floor(len(treemap) / stepy))):
        trees += treemap[stepy * x][(stepx * x) % linel] == '#'
    multi *= trees
print(multi)
