validpass = 0
for policy in [val.strip().split(' ') for val in open('input2').readlines()]:
    low, high = [int(i) - 1 for i in policy[0].split('-')]
    validpass += (policy[1][0] == policy[2][low]) != (policy[1][0] == policy[2][high])
print(validpass)
