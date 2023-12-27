import aoc, re

d = aoc.load(18)
d = [re.findall('\w+', i) for i in d]
x, y = 0, 0
vertices1 = []
for _, __, color in d:
    dir = 'RDLU'.index(_)
    dist = int(__)
    dx, dy = [(1, 0), (0, -1), (-1, 0), (0, 1)][int(dir)]
    x += dx*dist
    y += dy*dist
    vertices1.append((x, y))
x, y = 0, 0
vertices2 = []#[(x, y)]
for _, __, color in d:
    dir = color[-1]
    dist = int(color[:-1], 16)
    dx, dy = [(1, 0), (0, -1), (-1, 0), (0, 1)][int(dir)]
    x += dx*dist
    y += dy*dist
    vertices2.append((x, y))

def crop():
    xx = [i[0] for i in vertices[-6:]]
    yy = [i[1] for i in vertices[-6:]]
    shortest = 1<<31
    for i, z in enumerate(vertices):
        x, y = z
        xx = xx[1:] + [x]
        yy = yy[1:] + [y]
        if xx[2] != xx[3]: continue
        if (xx[2] - xx[1])*(xx[3]-xx[4]) < 0: continue
        if abs(xx[2] - xx[1]) < abs(xx[3] - xx[4]):
            if (yy[1] - yy[0])*(yy[2] - yy[3]) > 0: continue
        elif abs(xx[2] - xx[1]) > abs(xx[3] - xx[4]):
            if (yy[5] - yy[4])*(yy[2] - yy[3]) > 0: continue
        else:
            if (yy[1] - yy[0])*(yy[2] - yy[3]) > 0: continue
            if (yy[5] - yy[4])*(yy[2] - yy[3]) > 0: continue
        shortest = min(shortest, abs(yy[3]-yy[2]))
    for i, z in enumerate(vertices):
        x, y = z
        xx = xx[1:] + [x]
        yy = yy[1:] + [y]
        if xx[2] != xx[3]: continue
        if (xx[2] - xx[1])*(xx[3]-xx[4]) < 0: continue
        if abs(xx[2] - xx[1]) < abs(xx[3] - xx[4]):
            if (yy[1] - yy[0])*(yy[2] - yy[3]) > 0: continue
        elif abs(xx[2] - xx[1]) > abs(xx[3] - xx[4]):
            if (yy[5] - yy[4])*(yy[2] - yy[3]) > 0: continue
        else:
            if (yy[1] - yy[0])*(yy[2] - yy[3]) > 0: continue
            if (yy[5] - yy[4])*(yy[2] - yy[3]) > 0: continue
        if abs(yy[3] - yy[2]) > shortest: continue
        parity = 0 if xx[2] < xx[1] else 1
        px, py = vertices[-1]
        ty = max(yy[2], yy[3])
        for x, y in vertices:
            if x > xx[2] and max(py, y) >= ty and min(py, y) < ty: parity ^= 1
            py = y
        del vertices[i - 2]
        del vertices[i - (2 if i < 2 else 3)]
        if xx[1] == xx[4]:
            del vertices[i - (1 if i < 2 else (2 if i == 2 else 3))]
            del vertices[-1 if i < 4 else (i-4)]
        else:
            mi = min({1, 4}, key=lambda _:abs(xx[_]-xx[2]))
            if mi == 4:
                vertices[i - (1 if i < 2 else (2 if i == 2 else 3))] = (xx[4], yy[1])
            else:
                vertices[(i-2 if i < 2 else (-1 if i < 4 else i-4))] = (xx[1], yy[4])
        if parity == 1:
            return (min(abs(xx[2]-xx[1]),abs(xx[3]-xx[4])))*(abs(yy[1]-yy[4]) + 1)
        return -(min(abs(xx[2]-xx[1]),abs(xx[3]-xx[4])))*(abs(yy[1]-yy[4]) - 1)
    return cropy()
def cropy():
    shortest = 1<<31
    xx = [i[0] for i in vertices[-6:]]
    yy = [i[1] for i in vertices[-6:]]
    for i, z in enumerate(vertices):
        x, y = z
        yy = yy[1:] + [y]
        xx = xx[1:] + [x]
        if yy[2] != yy[3]: continue
        if (yy[2] - yy[1])*(yy[3]-yy[4]) < 0: continue
        if abs(yy[2] - yy[1]) < abs(yy[3] - yy[4]):
            if (xx[1] - xx[0])*(xx[2] - xx[3]) > 0: continue
        elif abs(yy[2] - yy[1]) > abs(yy[3] - yy[4]):
            if (xx[5] - xx[4])*(xx[2] - xx[3]) > 0: continue
        else:
            if (xx[1] - xx[0])*(xx[2] - xx[3]) > 0: continue
            if (xx[5] - xx[4])*(xx[2] - xx[3]) > 0: continue
        shortest = min(shortest, abs(xx[3]-xx[2]))
    for i, z in enumerate(vertices):
        x, y = z
        yy = yy[1:] + [y]
        xx = xx[1:] + [x]
        if yy[2] != yy[3]: continue
        if (yy[2] - yy[1])*(yy[3]-yy[4]) < 0: continue
        if abs(yy[2] - yy[1]) < abs(yy[3] - yy[4]):
            if (xx[1] - xx[0])*(xx[2] - xx[3]) > 0: continue
        elif abs(yy[2] - yy[1]) > abs(yy[3] - yy[4]):
            if (xx[5] - xx[4])*(xx[2] - xx[3]) > 0: continue
        else:
            if (xx[1] - xx[0])*(xx[2] - xx[3]) > 0: continue
            if (xx[5] - xx[4])*(xx[2] - xx[3]) > 0: continue
        if abs(xx[3]-xx[2]) > shortest: continue
        parity = 0 if yy[2] < yy[1] else 1
        px, py = vertices[-1]
        tx = max(xx[2], xx[3])
        for x, y in vertices:
            if y > yy[2] and max(px, x) >= tx and min(px, x) < tx: parity ^= 1
            px = x
        del vertices[i - 2]
        del vertices[i - (2 if i < 2 else 3)]
        if yy[1] == yy[4]:
            del vertices[i - (1 if i < 2 else (2 if i == 2 else 3))]
            del vertices[-1 if i < 4 else (i-4)]
        else:
            mi = min({1, 4}, key=lambda _:abs(yy[_]-yy[2]))
            if mi == 4:
                vertices[i - (1 if i < 2 else (2 if i == 2 else 3))] = (xx[1], yy[4])
            else:
                vertices[(i-2 if i < 2 else (-1 if i < 4 else i-4))] = (xx[4], yy[1])
        if parity == 1:
            return (min(abs(yy[2]-yy[1]),abs(yy[3]-yy[4])))*(abs(xx[1]-xx[4]) + 1)
        return -(min(abs(yy[2]-yy[1]),abs(yy[3]-yy[4])))*(abs(xx[1]-xx[4]) - 1)

part1 = 0
vertices = vertices1
while len(vertices) > 4:
    part1 += crop()
x1, y1 = vertices[0]
x2, y2 = vertices[2]
part1 += (abs(x2-x1)+1)*(abs(y2-y1)+1)

part2 = 0
vertices = vertices2
while len(vertices) > 4:
    part2 += crop()
x1, y1 = vertices[0]
x2, y2 = vertices[2]
part2 += (abs(x2-x1)+1)*(abs(y2-y1)+1)
