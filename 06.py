import aoc

d = aoc.loadints(6)

m = 1
for i, j in zip(d[0], d[1]):
    c = 0
    for t in range(100):
        dd = t*(i - t)
        if dd > j: c += 1
    m*=c
part1 = m
t = int(''.join(str(i) for i in d[0]))
dst = int(''.join(str(i) for i in d[1]))

part2 = t - 2*int((t - (t*t - 4*dst)**0.5)/2) - 1