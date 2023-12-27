import aoc
from math import lcm

d = aoc.load(8)
m = {i[:3]: (i[7:10], i[12:15]) for i in d[2:]}


z = [i for i in m if i[-1] == 'A']
AAA = z.index('AAA')
start = [-1 for i in range(len(z))]

i = 0
lr = d[0]
while -1 in start:
    for _ in range(len(z)):
        if z[_][-1] == 'Z':
            if start[_] == -1: start[_] = i
    z = [m[_][{'L':0,'R':1}[lr[i%len(lr)]]] for _ in z]
    i += 1
part1 = start[AAA]

while len(start) > 1:
    start.append(lcm(start.pop(), start.pop()))
part2 = start[0]