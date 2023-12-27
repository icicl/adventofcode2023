import aoc
d = aoc.load(23)
sy = len(d)
sx = len(d[0])

start = 1
end = 1j*(sy-1) + sx-2
def find(cur, past, part=1):
    while True:
        x,y = aoc.xy(cur)
        val = []
        for dir in {1,-1,1j,-1j} if d[y][x] == '.' else ({'<':{-1},'>':{+1},'^':{-1j},'v':{1j},'#':set()}[d[y][x]]):
            if cur + dir in past: continue
            x,y = aoc.xy(cur+dir)
            if not d[y][x] == '#':
                val += [cur+dir]
        if len(val) == 0: return -10000000
        if len(val) > 1:
            return max(find(v, past | {v}) for v in val)
        cur = val[0]
        past |= {cur}
        if cur == end: return len(past)
part1 = (find(start, set()))

start = (1, 0)
end = (sx-2, sy-1)
nodes = {start:{}, end:{}}
for y in range(1,sy-1):
    for x in range(1,sx-1):
        if d[y][x] != '#' and sum(d[y+dy][x+dx] != '#' for dx,dy in aoc.DXY) > 2:
            nodes[(x,y)] = {}

def routes(begin):
    x0, y0 = begin
    out = []
    for dx, dy in aoc.DXY:
        if not y0 + dy in range(sy): continue
        if d[y0+dy][x0+dx] != '#':
            count = 1
            prev = (x0,y0)
            x, y = x0+dx, y0+dy
            while not (x,y) in nodes:
                for ddx, ddy in aoc.DXY:
                    if d[y+ddy][x+ddx] != '#' and not (x+ddx, y+ddy) == prev:
                        break
                count += 1
                prev = (x, y)
                x += ddx
                y += ddy
            out += [[(x,y), count]]
    return out
rtes = {i:routes(i) for i in nodes}
part2 = (max(aoc.bfs(start, end, rtes)))