filepath = 'input6'

with open(filepath) as fp:
    line = fp.readline()
    group = ''
    count = 0
    while line:
        if line != '\n':
            group += line.strip()
        else:
            count += len(set(group))
            group = ''
        line = fp.readline()
    print(count)
