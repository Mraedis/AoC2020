from itertools import combinations

numlist = [int(num.strip()) for num in open('input9').readlines()]
found = 0
listlen = 2
target = 15353384

while found == 0:
    index = listlen
    while index < len(numlist):
        if sum(numlist[index-listlen:index]) == target:
            found = index
            print(max(numlist[index-listlen:index]) + min(numlist[index-listlen:index]))
            index = len(numlist)
        else:
            index += 1
    listlen += 1
