filepath = 'input1.1'
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

    found = False
    x = 0
    while not found:
        x2 = x + 1
        x3 = x2 + 1
        num1 = linelist[x]
        elesum = linelist[x] + linelist[x2] + linelist[x3]
        while elesum < 2020 and not found:
            x2 += 1
            x3 += x2 + 1
            elesum = linelist[x] + linelist[x2] + linelist[x3]
            while elesum < 2020 and not found:
                x3 += 1
                elesum = linelist[x] + linelist[x2] + linelist[x3]
            if elesum == 2020:
                eleproduct = linelist[x] * linelist[x2] * linelist[x3]
                found = True
                print(eleproduct)
        x += 1
