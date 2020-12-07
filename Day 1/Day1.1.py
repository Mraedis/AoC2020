from itertools import combinations
from math import prod

linelist = [int(val) for val in open('input1').readlines()]
pair = [pair for pair in combinations(linelist, 2) if sum(pair) == 2020][0]
print(prod(pair))
