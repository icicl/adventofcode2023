import aoc

d = aoc.load(15)[0]
def hash(s):
    val = 0
    for i in s:
        val = ((val + ord(i))*17)&255
    return val
part1 = (sum(hash(i) for i in d.split(',')))

boxes = [[] for _ in range(256)]
for i in d.split(','):
    if i[-1] == '-':
        label = i[:-1]
        box = hash(label)
        for j in boxes[box]:
            if j[0] == label:
                boxes[box].remove(j)
                break
    else:
        label = i[:-2]
        box = hash(label)
        val = int(i[-1])
        exists = False
        for j in boxes[box]:
            if j[0] == label:
                j[1] = val
                exists = True
                break
        if not exists:
            boxes[box].append([label, val])
    
part2 = (sum(sum((box + 1)*(idx + 1)*val[1] for idx, val in enumerate(boxes[box])) for box in range(256)))