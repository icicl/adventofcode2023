import aoc, re

d = aoc.load(22)

bricks = []
for i in d:
    bricks += [[]]
    c = [int(j) for j in re.findall('\d+', i)]
    for x in range(c[0], c[3] + 1):
        for y in range(c[1], c[4] + 1):
            for z in range(c[2], c[5] + 1):
                bricks[-1] += [[x,y,z]]
bricks.sort(key=lambda b:min(c[2] for c in b))

supporting = {}
supported = {}
blocks = {}
for n, brick in enumerate(bricks):
    for block in brick:
        blocks[tuple(block)] = n
    supporting[n] = set()
    supported[n] = set()

for n, brick in enumerate(bricks):
    halt = False
    while min(k[2] for k in brick) > 1:
        for block in brick:
            if (below := tuple(block[:2] + [block[2] - 1])) in blocks:
                if not blocks[below] == n:
                    supporting[blocks[below]].add(n)
                    supported[n].add(blocks[below])
                    halt = True
        if halt: break
        for block in brick:
            del blocks[tuple(block)]
            block[2] -= 1
            blocks[tuple(block)] = n
part1 = (sum(all(len(supported[i]) > 1 for i in supporting[j]) for j in supporting))

nodes = {i for i in supporting}
def fall(start):
    missing = {start}
    tofall = {i for i in supporting[start]}
    while tofall:
        i = tofall.pop()
        if len(supported[i] - missing) == 0:
            missing.add(i)
            tofall |= supporting[i]
    return len(missing) - 1
part2 = (sum(fall(i) for i in nodes))