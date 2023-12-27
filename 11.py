import aoc
from itertools import combinations as co
from itertools import product as pr
d = aoc.load(11)
lx, ly = len(d[0]), len(d)
galaxies = [(x,y) for x,y in pr(range(lx), range(ly)) if d[y][x] == '#']
dup_x = {x for x in range(lx) if all(d[y][x] == '.' for y in range(ly))}
dup_y = {y for y in range(ly) if not '#' in d[y]}
dist = 0
space = 0
for i, j in co(galaxies, 2):
    x1, x2 = sorted([i[0], j[0]])
    y1, y2 = sorted([i[1], j[1]])
    dist += x2 - x1 + y2 - y1
    space += len(dup_x & set(range(x1, x2)))
    space += len(dup_y & set(range(y1, y2)))
part1 = dist + space
part2 = dist + space*999999