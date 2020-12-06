filepath = 'input2'

validpass = 0

with open(filepath) as fp:
    line = fp.readline()
    while line:
        policy, passkey, password = line.split(' ')
        lowpol, uppol = policy.split('-')
        if (password[int(lowpol)-1] == passkey[0]) != (password[int(uppol)-1] == passkey[0]):
            validpass += 1
        line = fp.readline()
    print(validpass)
