import aoc
d = aoc.load(13, raw=True).split('\n\n')

def score(p):
    px, py = len(p[0]), len(p)
    res = set()
    for x in range(1,px):
        if all(all(p[y][i] == p[y][2*x - 1 - i] for i in range(max(2*x - px, 0), x)) for y in range(py)):
            res.add(x)
    for y in range(1, py):
        if all(all(p[i][x] == p[2*y - 1 - i][x] for i in range(max(2*y - py, 0), y)) for x in range(px)):
            res.add(100*y)
    return res
part1 = (sum(score(i.split('\n')).pop() for i in d))

def flip(s):
    return '.' if s == '#' else '#'
def score2(p):
    p = [[i for i in j] for j in p.split('\n')]
    ignore = score(p).pop()
    p[-1][-1] = flip(p[-1][-1])
    for y in range(len(p)):
        for x in range(len(p[0])):
            if x == 0: p[y - 1][-1] = flip(p[y - 1][-1])
            else: p[y][x - 1] = flip(p[y][x - 1])
            p[y][x] = flip(p[y][x])
            s = score(p)
            s -= {ignore}
            if s: return s.pop()
    return -1
part2 = (sum(score2(i) for i in d))