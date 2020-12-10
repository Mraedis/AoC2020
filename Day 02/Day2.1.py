validpass = 0
for policy in [val.strip().split(' ') for val in open('input2').readlines()]:
    low, high = [int(i) for i in policy[0].split('-')]
    validpass += policy[2].count(policy[1][0]) in range(low, high)
print(validpass)
