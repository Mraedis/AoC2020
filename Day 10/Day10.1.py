adaptlist = [0] + sorted(int(num.strip()) for num in open('input10').readlines())

diff = {1: 0, 2: 0, 3: 1}

for x in range(1, len(adaptlist)):
    diff[adaptlist[x] - adaptlist[x - 1]] += 1

print(diff[1] * diff[3])
