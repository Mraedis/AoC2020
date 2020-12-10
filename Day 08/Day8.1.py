oplist = [[op for op in line.strip().split(' ')] for line in open('input8').readlines()]
acc = 0
run = []
lastrun = 0
while lastrun not in run:
    run.append(lastrun)
    op = oplist[lastrun]
    acc += (op[0] == 'acc') * int(op[1])
    lastrun += (op[0] == 'nop') + (op[0] == 'acc') + (op[0] == 'jmp') * int(op[1])
print(acc)
