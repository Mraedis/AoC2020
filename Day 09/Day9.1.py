from itertools import combinations

numlist = [int(num.strip()) for num in open('input9').readlines()]
found = 0
index = 25

while found == 0:
    pair = [pair for pair in combinations(numlist[index-25:index], 2) if sum(pair) == numlist[index]]
    if len(pair) >= 1:
        index += 1
    else:
        found = numlist[index]
print(found)
