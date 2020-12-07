filepath = 'input7'

baglist = {}

with open(filepath) as fp:
    line = fp.readline()
    while line:
        container, contents = line.split(' bags contain')
        cner_color = container.split('bag')[0]
        baglist[container] = {}
        for bag in contents.rsplit(' ', 1)[0].split(', '):
            amount, b_color = bag.replace('bags', 'bag').split('bag')[0].strip().split(' ', 1)
            baglist[container][b_color] = amount
        line = fp.readline()

old_bcount = 0
bcount = 0
bag_check = []
for upper_bag in baglist:
    for lower_bag in baglist[upper_bag]:
        if lower_bag == 'shiny gold':
            bag_check.append(upper_bag)
            bcount += 1

while bcount != old_bcount:
    bchk_temp = []
    old_bcount = bcount
    for upper_bag in baglist:
        for lower_bag in baglist[upper_bag]:
            if lower_bag in bag_check:
                if upper_bag not in bag_check and upper_bag not in bchk_temp:
                    bchk_temp.append(upper_bag)
                    bcount += 1
    for bag in bchk_temp:
        bag_check.append(bag)

print(bcount)
