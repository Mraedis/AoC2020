inp = open('input16').readlines()
fields = {}
for line in inp[:20]:
    field, ranges = line.strip().split(': ')
    fields[field] = ranges.split(' or ')

for field in fields.keys():
    range1, range2 = fields[field]
    fields[field] = [int(x) for x in range1.split('-')] + [int(x) for x in range2.split('-')]

ticketlist = [[int(num) for num in line.strip().split(',')] for line in inp[25:]]
invalid = 0
for ticket in ticketlist:
    for num in ticket:
        valid = 0
        for _, field in fields.items():
            valid += num in range(field[0], field[1] + 1) or num in range(field[2], field[3] + 1)
        invalid += int(num) * (valid <= 0)
print(invalid)
