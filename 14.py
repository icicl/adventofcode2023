import aoc

d = aoc.load(14)
sy = len(d)
sx = len(d[0])


static = set()
static_x = {}
static_y = {}
static_x_rev = {}
static_y_rev = {}
mobile = set()

for x in range(sx):
    static_x[x] = [-1]
for y in range(sy):
    static_y[y] = [-1]
    for x in range(sx):
        if d[y][x] == '#':
            static.add((x, y))
            static_x[x].append(y)
            static_y[y].append(x)
        elif d[y][x] == 'O':
            mobile.add((x, y))
    static_y[y] += [sx]
for x in range(sx):
    static_x[x] += [sy]

for i in static_x: static_x_rev[i] = static_x[i][::-1]
for i in static_y: static_y_rev[i] = static_y[i][::-1]

def load(mobile):
    return int(sum(sy -y for x,y in mobile))

def tilt(m, dir):
    out = set()
    if dir == -1j:
        for x,y in m:
            for yy in static_x_rev[x]:
                if yy < y:
                    break
            yy += 1
            while (x, yy) in out or (x, yy) in static:
                yy += 1
            out.add((x, yy))
    elif dir == +1j:
        for x,y in m:
            for yy in static_x[x]:
                if yy > y:
                    break
            yy -= 1
            while (x, yy) in out or (x, yy) in static:
                yy -= 1
            out.add((x, yy))
    elif dir == -1:
        for x,y in m:
            for xx in static_y_rev[y]:
                if xx < x:
                    break
            xx += 1
            while (xx, y) in out or (xx, y) in static:
                xx += 1
            out.add((xx, y))
    elif dir == +1:
        for x,y in m:
            for xx in static_y[y]:
                if xx > x:
                    break
            xx -= 1
            while (xx, y) in out or (xx, y) in static:
                xx -= 1
            out.add((xx, y))
    return out

part1 = (load(tilt(mobile, -1j)))

def cycle(m):
    for i in (-1j, -1, 1j, 1):
        m = tilt(m, i)
    return m

prev = {}
score = {}
count = 0

while not tuple(mobile) in prev:
    prev[tuple(mobile)] = count
    score[count] = load(mobile)
    count += 1
    mobile = cycle(mobile)
lim = 10**9
part2 = (score[(lim - count)%(count - prev[tuple(mobile)]) + prev[tuple(mobile)]])