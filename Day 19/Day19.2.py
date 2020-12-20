import re


def inner(part):
    cnt = 0
    while any(char.isdigit() for char in part) and cnt < 120:
        part = re.sub('(\d+)\s*', lambda mtch: rules[int(mtch.group(0))], part)
        cnt += 1
    print()
    return part


inp, messages = [line.rstrip('\n') for line in open('input19').read().split('\n\n')]
rules = dict((int(i.split(': ', 1)[0]), i.split(': ', 1)[1]) for i in inp.split('\n'))

for r in rules.keys():
    if r == 8:
        rules[r] = '42 | 42 8'
    elif r == 11:
        rules[r] = '42 31 | 42 11 31'
    rules[r] = '(' + rules[r].strip('"').replace(' | ', '|') + ')'

obey = rules[0]

count = 0
pattern = inner(obey)
for msg in messages.split('\n'):
    count += bool(re.fullmatch(pattern, msg))
print(count)
