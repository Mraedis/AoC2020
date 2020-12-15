inp = [0, 14, 1, 3, 7, 9]


def lrindex(alist, value):
    return len(alist) - alist[-1::-1].index(value) if value in alist else -1


turns = []
for num in inp:
    turns.append(num)
turns.append(0)

while len(turns) <= 2020:
    ind = lrindex(turns[:-1], turns[-1])
    if ind > -1:
        turns.append(len(turns) - ind)
    else:
        turns.append(0)
print(turns[2019])
