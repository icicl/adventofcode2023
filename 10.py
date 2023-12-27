import aoc
d = aoc.load(10)
d = [' ' + _ + ' ' for _ in d]
d = [' '*len(d[0])] + d + [' '*len(d[0])]

for y in range(len(d)):
    for x in range(len(d[0])):
        if d[y][x] == 'S':
            loc = (x,y)
east = '-LFS'
south = '|7FS'
west = '-J7S'
north = '|LJS'

q = {loc}
path = set()
count = -1
while q:
    path |= q
    q2 = set()
    while q:
        x,y = q.pop()
        if d[y][x] in east and d[y][x+1] in west:
            q2.add((x+1, y))
        if d[y][x] in south and d[y+1][x] in north:
            q2.add((x, y+1))
        if d[y][x] in west and d[y][x-1] in east:
            q2.add((x-1, y))
        if d[y][x] in north and d[y-1][x] in south:
            q2.add((x, y-1))
    q = q2 - path
    count += 1
part1 = count

sets = []
past = set() | path
for yy in range(len(d)):
    for xx in range(len(d[0])):
        if not (xx,yy) in past:
            cur_past = set()
            q = {(xx,yy)}
            sets += [set()]
            while q:
                x, y = q.pop()
                sets[-1].add((x, y))
                for dx, dy in [[1,0],[0,1],[0,-1],[-1,0]]:
                    if x + dx >= 0 and x + dx < len(d[0]) and y + dy >= 0 and y + dy < len(d):
                        q.add((x+dx, y+dy))
                q -= path
                q -= cur_past
                cur_past |= {(x,y)}
            past |= cur_past

vert = '7F|' # S just for me - depending on which piece S acts as this may include the S tile
tot = 0
inn2 = set()
for k in sets[1:]:
    for x, y in k:
        s = 0
        s2 = 0
        for i in range(x):
            if (i,y) in path and d[y][i] in vert:
                s += 1
        if s&1:
            tot += 1
            inn2.add((x,y))
part2 = tot