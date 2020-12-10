
import json
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
    validpasses += len(passport.keys()) > 7 or (len(passport.keys()) > 6 and 'cid' not in passport)
print(validpasses)
