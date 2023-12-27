import aoc

d = aoc.load(5)

def dest(src, map_):
    for i in map_:
        if src in range(i[1], i[1]+i[2]):
            return i[0] + src - i[1]
    return src

seeds = aoc.ints(d[0])
maps = []
b = 0
for i in d:
    if i == '':
        b = 0
    if b:
        maps[-1] += [aoc.ints(i)]
    if 'map:' in i:
        maps += [[]]
        b = 1
mm = []
for i in seeds:
    for j in maps:
        i = dest(i, j)
    mm += [i]
part1 = min(mm)

for ii in maps:
    for i in ii:
        i[0] -= i[1]

ranges = []
for i in range(0,len(seeds),2):
    ranges += [(seeds[i], seeds[i + 1])]

for m in maps: ### TODO rewrite using aoc.Range
    r2 = []
    while ranges:
        c = ranges.pop()
        a,b = c
        for i,j,k in m:
            if a+b <= j or a >= j+k:
                continue
            z1 = a <= j
            z2 = a+b >= j+k
            if z1 and z2:
                r2 += [(j+i,k)]
                ranges += [(a, j-a), (j+k, a+b-j-k)]
            elif z1:
                r2 += [(j+i, a+b-j)]
                ranges += [(a, j-a)]
            elif z2:
                r2 += [(a+i, j+k-a)]
                ranges += [(j+k, a+b-j-k)]
            else:
                r2 += [(a+i,b)]
    ranges = r2
part2 = min(i[0] for i in ranges)