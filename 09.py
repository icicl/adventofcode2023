import aoc

d = aoc.loadints(9)

def proc(h, part1):
    d = [h]
    while any(bool(i) for i in d[-1]):
        d += [[d[-1][i]-d[-1][i-1] for i in range(1,len(d[-1]))]]
    for i in range(len(d)-1,0,-1):
        d[i-1] = [d[i-1][0] - d[i][0]] + d[i-1] + [d[i-1][-1] + d[i][-1]]
    return d[0][-1] if part1 else d[0][0]

part1 = sum(proc(i, True) for i in d)
part2 = sum(proc(i, False) for i in d)
