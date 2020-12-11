oplist = [[op for op in line.strip().split(' ')] for line in open('input8').readlines()]
change = 0

for x in range(0, len(oplist)):
    if oplist[x][0] in ['jmp', 'nop']:
        oplist[x][0] = 'jmp' if oplist[x][0] == 'nop' else 'nop'
        acc = 0
        run = []
        lastrun = 0
        while lastrun not in run and lastrun < len(oplist):
            run.append(lastrun)
            op = oplist[lastrun]
            acc += (op[0] == 'acc') * int(op[1])
            lastrun += (op[0] == 'nop') + (op[0] == 'acc') + (op[0] == 'jmp') * int(op[1])
        if lastrun == len(oplist):
            change = acc
        oplist[x][0] = 'jmp' if oplist[x][0] == 'nop' else 'nop'
print(change)
