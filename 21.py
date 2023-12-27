import aoc

d = aoc.load(21)
sx, sy = len(d[0]), len(d)
path = set()
for y in range(sy):
    for x in range(sx):
        if d[y][x] == '.':
            path.add(x + 1j*y)
        elif d[y][x] == 'S':
            path.add(x + 1j*y)
            start = x + 1j*y

current = {start}
for _ in range(64):
    next = set()
    for tile in current:
        for dir in {1,-1,1j,-1j}:
            if tile + dir in path:
                next.add(tile + dir)
    current = next
part1 = (len(current))

def clip(tile):
    return int(tile.real)%sx + 1j*(int(tile.imag)%sy)

current = {start}
target = 26501365
counts = []
safety = 2
past = set()
count = [0, 0]
parity = 0
for _ in range(safety*sy+target%sy):
    past |= current
    count[parity] += len(current)
    parity ^= 1
    next = set()
    for tile in current:
        for dir in {1,-1,1j,-1j}:
            if clip(tile + dir) in path and not tile + dir in past:
                next.add(tile + dir)
    current = next
counts += [count[parity] + len(current)]
for __ in range(2):
    for _ in range(sy):
        past |= current
        count[parity] += len(current)
        parity ^= 1
        next = set()
        for tile in current:
            for dir in {1,-1,1j,-1j}:
                if clip(tile + dir) in path and not tile + dir in past:
                    next.add(tile + dir)
        current = next
    counts += [count[parity] + len(current)]

aa = (counts[2] - 2*counts[1] + counts[0])//2
bb = (counts[1] - counts[0]) - (safety*2 + 1)*aa
cc = counts[0] - aa*safety**2 - bb*safety

xx = target // sy
part2 = (aa*xx**2 + bb*xx + cc)

