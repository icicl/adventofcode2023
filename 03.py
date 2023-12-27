import aoc

d = aoc.load(3)

nums = set()

for y in range(len(d)):
    c = 0
    val = False
    for x in range(len(d[0])):
        if d[y][x].isdigit():
            c += 1
        else:
            if c:
                nums.add((x - c, y, c))
            c = 0
    if c:
        nums.add((x + 1 - c, y, c))

part1 = 0
for x,y,c in nums:
    delta = 0
    for xx in range(max(0, x - 1), min(x + c + 1, len(d[0]))):
        for yy in range(max(0, y - 1), min(y + 2, len(d))):
            if not d[yy][xx] in '0123456789.':
                delta = int(d[y][x:x+c])
    part1 += delta

part2 = 0
for y in range(len(d)):
    for x in range(len(d[0])):
        if d[y][x] == '*':
            rprod = 1
            rcount = 0
            for i, j, l in nums:
                if abs(j - y) <= 1 and i + l >= x and i < x + 2:
                    rprod *= int(d[j][i:i+l])
                    rcount += 1
            if rcount == 2:
                part2 += rprod



