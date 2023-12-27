import aoc

d = aoc.load(16)
ly, lx = len(d), len(d[0])

t = {}
for y in range(len(d)):
    for x in range(len(d[y])):
        t[x + 1j*y] = d[y][x]

def count(start_loc, start_dir):
    prev = {}
    cur = {(start_loc, start_dir)}
    while cur:
        loc, dir = cur.pop()
        if not loc in t: continue
        if loc in prev:
            if dir in prev[loc]:
                continue
            else:
                prev[loc].add(dir)
        else:
            prev[loc] = {dir}
        tile = t[loc]
        if tile == '.': cur.add((loc + dir, dir))
        elif tile == '/':
            dir = {1:-1j, -1j:1, -1:1j, 1j:-1}[dir]
            cur.add((loc + dir, dir))
        elif tile == '\\':
            dir = {1:1j, 1j:1, -1:-1j, -1j:-1}[dir]
            cur.add((loc + dir, dir))
        elif tile == '-':
            if dir in {1, -1}:
                cur.add((loc + dir, dir))
            else:
                cur.add((loc + 1, +1))
                cur.add((loc - 1, -1))
        elif tile == '|':
            if dir in {1j, -1j}:
                cur.add((loc + dir, dir))
            else:
                cur.add((loc + 1j, +1j))
                cur.add((loc - 1j, -1j))
    return len(prev)
part1 = (count(0, 1))

part2 = 0
part2 = max(part2, max(count(y*1j, 1) for y in range(ly)))
part2 = max(part2, max(count(lx-1 + y*1j, -1) for y in range(ly)))
part2 = max(part2, max(count(x, 1j) for x in range(lx)))
part2 = max(part2, max(count(x + 1j*(ly-1), -1j) for x in range(lx)))
