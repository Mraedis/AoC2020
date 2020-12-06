filepath = 'input6'

with open(filepath) as fp:
    line = fp.readline()
    group = ''
    count = 0
    gcount = 0
    while line:
        if line != '\n':
            group += line.strip()
            gcount += 1
        else:
            freqmap = {}
            for c in group:
                freqmap[c] = freqmap.get(c, 0) + 1
            for f in freqmap.values():
                if f == gcount:
                    count += 1
            group = ''
            gcount = 0
        line = fp.readline()
    print(count)
