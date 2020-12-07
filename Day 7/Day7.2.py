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
bcount = len(baglist['shiny gold'])
counted = 0
bag_check = {'shiny gold': 1}
bchk_temp = {}

while bcount != old_bcount:
    old_bcount = bcount
    for upper_bag in bag_check:
        for lower_bag in baglist[upper_bag]:
            if 'other' not in lower_bag:
                if lower_bag in bchk_temp:
                    bchk_temp[lower_bag] += int(bag_check[upper_bag]) * int(baglist[upper_bag][lower_bag])
                else:
                    bchk_temp[lower_bag] = int(bag_check[upper_bag]) * int(baglist[upper_bag][lower_bag])
                bcount += 1
    if bcount != old_bcount:
        bag_check = bchk_temp
        for bag in bchk_temp:
            counted += bchk_temp[bag]
    bchk_temp = {}
print(counted)
