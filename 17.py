import aoc

d = aoc.load(17)

tiles = {}
for y in range(len(d)):
    for x in range(len(d[y])):
        tiles[x + 1j*y] = int(d[y][x])
dir = 1
ns = {0:0, 1j:tiles[1j], 2j:tiles[1j]+tiles[2j], 3j:tiles[1j]+tiles[2j]+tiles[3j]} # ending points for ns run
ew = {}
queue = {i for i in ns}
while queue:
    new_queue = set()
    end = ew if dir == 1 else ns
    for i in queue:
        score = ns[i] if dir == 1 else ew[i]
        to = i
        for streak in range(3):
            to += dir
            if not to in tiles: break
            score += tiles[to]
            if (not to in end) or end[to] > score:
                end[to] = score
                new_queue.add(to)
        ##### ^ forwards ^    v backwards v #####
        score = ns[i] if dir == 1 else ew[i]
        to = i
        for streak in range(3):
            to -= dir
            if not to in tiles: break
            score += tiles[to]
            if (not to in end) or end[to] > score:
                end[to] = score
                new_queue.add(to)
    queue = new_queue
    dir = 1j if dir == 1 else 1

def res(xy):
    m = 10**9
    if xy in ew: m = ew[xy]
    if xy in ns: m = min(m, ns[xy])
    return m
part1 = res((len(d[0])-1)+1j*(len(d)-1))

dir = 1
ns = {0:0}
sc = 0
for y in range(3):
    sc += tiles[y*1j]
for y in range(4,11):
    sc += tiles[y*1j]
    ns[1j*y] = sc # ending points for ns run
ew = {}
queue = {i for i in ns}
while queue:
    new_queue = set()
    end = ew if dir == 1 else ns
    for i in queue:
        score = ns[i] if dir == 1 else ew[i]
        to = i
        for streak in range(3):
            to += dir
            if not to in tiles: break
            score += tiles[to]
        for streak in range(7):
            to += dir
            if not to in tiles: break
            score += tiles[to]
            if (not to in end) or end[to] > score:
                end[to] = score
                new_queue.add(to)
        #####
        score = ns[i] if dir == 1 else ew[i]
        to = i
        for streak in range(3):
            to -= dir
            if not to in tiles: break
            score += tiles[to]
        for streak in range(7):
            to -= dir
            if not to in tiles: break
            score += tiles[to]
            if (not to in end) or end[to] > score:
                end[to] = score
                new_queue.add(to)
    queue = new_queue
    dir = 1j if dir == 1 else 1
part2 = res((len(d[0])-1)+1j*(len(d)-1))
