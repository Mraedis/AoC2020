foodlist = [line.rstrip('\n') for line in open('input21').read().split('\n')]

matchlist = {}
allingrs = []
ingredients = set()
for fl in foodlist:
    ingr, al = fl.split(' (contains ')
    for alrgn in al[:-1].split(', '):
        if alrgn in matchlist.keys():
            matchlist[alrgn][0].update(set(ingr.split(' ')))
        else:
            matchlist[alrgn] = [set(ingr.split(' '))]
        matchlist[alrgn].append(ingr.split(' '))
        ingredients.update(set(ingr.split(' ')))
    allingrs.extend(ingr.split(' '))

possibles = set()
for mtch in matchlist:
    diff = matchlist[mtch][0]
    for s in matchlist[mtch][1:]:
        diff.intersection_update(set(s))
    possibles.update(diff)

sieve = {}
target = len(possibles)

for k in matchlist.keys():
    matchlist[k] = matchlist[k].pop(0)

while len(sieve) < target:
    s = {}
    for name, options in matchlist.items():
        if len(options) == 1:
            s[name] = options

    for name, option in s.items():
        sieve[name] = option
        for n, o in matchlist.items():
            matchlist[n] = matchlist[n] - option

klist = []
prnt = ''
for k in sorted(sieve.keys()):
    prnt += ',' + str(sieve[k].pop())
print(prnt[1:])
