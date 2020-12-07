validpass = 0
policylist = [val.strip().split(' ') for val in open('input2').readlines()]
for policy in policylist:
    low, high = [int(i) for i in policy[0].split('-')]
    validpass += policy[2].count(policy[1][0]) in range(low, high)
print(validpass)
