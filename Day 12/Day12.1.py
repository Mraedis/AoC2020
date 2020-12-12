pos = [0, 0]
vec = [1, 0]
dvec = [[1, 0], [0, 1], [-1, 0], [0, -1]]

instrmap = [[line.strip()[0], int(line.strip()[1:])] for line in open('input12').readlines()]
for instr in instrmap:
    if instr[0] == 'R':
        vec = dvec[(dvec.index(vec) + 4 - int(instr[1] / 90)) % 4]
    elif instr[0] == 'L':
        vec = dvec[(dvec.index(vec) + int(instr[1] / 90)) % 4]
    elif instr[0] == 'E':
        pos[0] += instr[1]
    elif instr[0] == 'N':
        pos[1] += instr[1]
    elif instr[0] == 'W':
        pos[0] -= instr[1]
    elif instr[0] == 'S':
        pos[1] -= instr[1]
    elif instr[0] == 'F':
        pos[0] += instr[1] * vec[0]
        pos[1] += instr[1] * vec[1]
    print(abs(pos[0]) + abs(pos[1]))
