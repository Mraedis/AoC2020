import math

trees = 0
stepx = 3
stepy = 1

treemap = [[c for c in val.strip()] for val in open('input3').readlines()]
linel = len(treemap[0])

for x in range(1, int(math.floor(len(treemap) / stepy))):
    trees += treemap[stepy * x][(stepx * x) % linel] == '#'
print(trees)
