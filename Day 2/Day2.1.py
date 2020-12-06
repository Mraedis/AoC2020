filepath = 'input2'

validpass = 0

with open(filepath) as fp:
    line = fp.readline()
    while line:
        policy, passkey, password = line.split(' ')
        numkey = password.count(passkey[0])
        lowpol, uppol = policy.split('-')
        if int(lowpol) <= numkey <= int(uppol):
            validpass += 1
        line = fp.readline()
    print(validpass)
