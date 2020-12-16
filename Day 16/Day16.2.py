inp = open('input16').readlines()
fields = {}
for line in inp[:20]:
    field, ranges = line.strip().split(': ')
    fields[field] = ranges.split(' or ')

for field in fields.keys():
    range1, range2 = fields[field]
    fields[field] = [int(x) for x in range1.split('-')] + [int(x) for x in range2.split('-')]

ticketlist = [[int(num) for num in line.strip().split(',')] for line in inp[25:]]

myticket = [int(num) for num in inp[22].strip().split(',')]
newlist = [myticket]
for ticket in ticketlist:
    invalid = 0
    for num in ticket:
        valid = 0
        for _, field in fields.items():
            valid += num in range(field[0], field[1]+1) or num in range(field[2], field[3]+1)
        invalid += num * (valid <= 0)
    if not invalid:
        newlist.append(ticket)

rulelist = {}
for num in range(len(myticket)):
    for name, field in fields.items():
        valid = all(ticket[num] in range(field[0], field[1]+1) or ticket[num] in range(field[2], field[3]+1)
                    for ticket in newlist)
        if valid:
            if name in rulelist.keys():
                rulelist[name].add(num)
            else:
                rulelist[name] = {num}
sieve = {}
target = len(rulelist)
while len(sieve) < target:
    s = {}
    for name, options in rulelist.items():
        if len(options) == 1:
            s[name] = options

    for name, option in s.items():
        sieve[name] = option
        for n, o in rulelist.items():
            rulelist[n] = rulelist[n] - option

product = 1
for s in sieve.keys():
    if 'departure' in s:
        for ts in sieve[s][0]:
            product *= myticket[ts]
print(product)
