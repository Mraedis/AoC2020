pos = 0+0j
wp = 10+1j
dvec = {'N': 0 + 1j, 'E': 1 + 0j, 'S': 0 - 1j, 'W': -1 + 0j}

instrmap = [[line.strip()[0], int(line.strip()[1:])] for line in open('input12').readlines()]
for instr in instrmap:
    if instr[0] == 'L':
        for x in range(int(instr[1]/90)):
            wp *= 1j
    elif instr[0] == 'R':
        for x in range(int(instr[1]/90)):
            wp *= -1j
    elif instr[0] == 'F':
        pos += instr[1] * wp
    else:
        wp += dvec[instr[0]] * instr[1]
print(abs(pos.real) + abs(pos.imag))
