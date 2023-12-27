import aoc

d = aoc.loadints(4)

p = []
for i in d:
    t = 0
    for j in i[11:]:
        if j in i[1:11]:
            t += 1
    p += [t]
part1 = sum(1<<(i-1) if i else 0 for i in p)

v = [1]*len(p)
for i in range(len(p)):
    for j in range(i + 1, min(len(p), p[i] + i + 1)):
        v[j] += v[i]
part2 = sum(v)
