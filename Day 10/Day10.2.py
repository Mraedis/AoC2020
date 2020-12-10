adaptlist = [0] + sorted(int(num.strip()) for num in open('input10').readlines())

paths = [1] + [0] * (len(adaptlist) - 1)

for x, adapter in enumerate(adaptlist):
    for y in range(x - 3, x):
        if adapter - adaptlist[y] <= 3:
            paths[x] += paths[y]

print(paths[-1])
