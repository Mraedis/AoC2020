filepath = 'input1'
som = 0

with open(filepath) as fp:
    line = fp.readline()
    linelist = []
    listlength = 0
    while line:
        linelist.append(int(line))
        line = fp.readline()
        listlength += 1
    linelist.sort()

    for x in range(0, listlength):
        x2 = x + 1
        num1 = linelist[x]
        elesum = linelist[x] + linelist[x2]
        while elesum < 2020:
            x2 += 1
            elesum = linelist[x] + linelist[x2]
        if elesum == 2020:
            eleproduct = linelist[x] * linelist[x2]
            print(eleproduct)
            break