validpass = 0
policylist = [val.strip().split(' ') for val in open('input2').readlines()]
for policy in policylist:
    low, high = [int(i) - 1 for i in policy[0].split('-')]
    validpass += (policy[1][0] == policy[2][low]) != (policy[1][0] == policy[2][high])
print(validpass)
