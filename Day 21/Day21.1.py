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

impossibles = ingredients.difference(possibles)
print(sum(allingrs.count(i) for i in impossibles))
