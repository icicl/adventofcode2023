import aoc, re
from itertools import combinations as co

d = aoc.load(24)
d = [[int(i) for i in re.findall('-?\d+', j)] for j in d]

low = 200000000000000
high = 400000000000000

def intersect(a, b):
    m0 = a[4]/a[3]
    m1 = b[4]/b[3]
    x0, y0 = a[:2]
    x1, y1 = b[:2]
    if m0 == m1: return -1, -1
    x = (m0*x0-m1*x1 + y1-y0) / (m0-m1)
    y = m0*(x-x0)+y0
    return x, y

part1 = 0
for i, j in co(d, 2):
    x, y = intersect(i, j)
#    print(i, j, x, y)
    if x >= low and x <= high and y >= low and y <= high:
        if (x > i[0] and i[3] < 0) or (x < i[0] and i[3] > 0):
            continue
        if (x > j[0] and j[3] < 0) or (x < j[0] and j[3] > 0):
            continue
        part1 += 1

vels = [0,0,0]

for idx in range(3):
    possible = set()
    for i, j in co(d, 2):
        if i[3 + idx] == j[3 + idx]:
            dx = abs(i[idx]-j[idx])
            if dx == 0: continue
            f = aoc.divisors(dx)
            valid = set()
            for k in f:
                valid.add(k + i[3+idx])
                valid.add(-k + i[3+idx])
            if not possible: possible = valid
            else: possible &= valid
    vels[idx] = possible.pop()


xyz = [0,0,0]
for idx in range(3):
    i2 = (idx+1)%3
    possible = set()
    for i, j in co(d, 2):
        if i[3 + i2] == j[3 + i2] and (i[3 + idx] != j[3 + idx]) and i[3 + i2] != vels[i2]:
            dt = (j[i2]-i[i2]) / (vels[i2]-i[3+i2])
            ta = (dt*(vels[idx]-j[3+idx]) - (j[idx]-i[idx])) / (j[3+idx] - i[3+idx])
            pos = i[idx] + ta*(i[3+idx]-vels[idx])
            xyz[idx] = pos
            break
part2 = (int(sum(xyz)))