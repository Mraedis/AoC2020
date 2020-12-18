import re

homework = [line.strip() for line in open('input18').readlines()]


def inner(part):
    while '+' in part:
        part = re.sub('(\d+)\s*\+\s*(\d+)', lambda mtch: str(eval(mtch.group(0))), part)
    while '*' in part:
        part = re.sub('(\d+)\s*\*\s*(\d+)', lambda mtch: str(eval(mtch.group(0))), part)
    return part


total = 0
for line in homework:
    while '(' in line:
        line = re.sub(r'\(([^()]+)\)', lambda mtch: inner(mtch.group(1)), line)
    total += int(inner(line))
print(total)
