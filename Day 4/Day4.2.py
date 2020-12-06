import json
import re
filepath = 'input4'

passlist = []

with open(filepath) as fp:
    line = fp.readline()
    currentpass = ''
    while line:
        if line == "\n":
            passlist.append("{\"" + currentpass.strip().replace(" ", "\",\"").replace(":", "\":\"") + "\"}")
            currentpass = ''
        else:
            currentpass += ' ' + line.strip()
        line = fp.readline()
    passlist.append("{\"" + currentpass.strip().replace(" ", "\",\"").replace(":", "\":\"") + "\"}")

parsedpass = list(map(lambda x: json.loads(x), passlist))
validpasses = 0

for passport in parsedpass:
    if len(passport.keys()) > 7 or (len(passport.keys()) > 6 and 'cid' not in passport):
        if 1919 < int(passport['byr']) < 2003 and 2009 < int(passport['iyr']) < 2021 and len(passport['eyr']) == 4:
            if 2019 < int(passport['eyr']) < 2031 and re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport['hcl']):
                if len(passport['pid']) == 9 and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    if passport['pid'].isdigit():
                        if passport['hgt'][-2:] == 'in' and 58 < int(passport['hgt'][:-2]) < 77:
                            validpasses += 1
                        elif passport['hgt'][-2:] == 'cm' and 149 < int(passport['hgt'][:-2]) < 194:
                            validpasses += 1
print(validpasses)
