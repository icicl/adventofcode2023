import aoc
d = aoc.load(20)
modules = {}
flip = {}
con = {}
for i in d:
    if i[0] == '%': kind = 1
    elif i[0] == '&': kind = 2
    else: kind = 0
    name, dest = i[(kind + 1)//2:].split(' -> ')
    dest = dest.split(', ')
    modules[name] = dest
    if kind == 1: flip[name] = 0
    elif kind == 2: con[name] = {}
for i in con:
    for j in modules:
        if i in modules[j]: con[i][j] = 0

for i in flip: flip[i] = 0
for i in con:
    for j in con[i]: con[i][j] = 0

sent = [0, 0]
for __ in range(1000):
    sent[0] += 1 + len(modules['broadcaster'])
    pulses = [(i, 0, 'broadcaster') for i in modules['broadcaster']]
    while pulses:
        dest, pulse, src = pulses[0]
        del pulses[0]
        if dest in flip:
            if pulse == 0:
                flip[dest] = 1 - flip[dest]
                for j in modules[dest]:
                    sent[flip[dest]] += 1
                    pulses.append((j, flip[dest], dest))
        elif dest in con:
            con[dest][src] = pulse
            out = int(any(con[dest][k] == 0 for k in con[dest]))
            for j in modules[dest]:
                sent[out] += 1
                pulses.append((j, out, dest))
part1 = (aoc.pi(sent))

part2 = 1
for start in modules['broadcaster']:
    cycle = 0
    power = 0
    node = modules[start]
    center = node[0] if node[0] in con else node[1]
    while True:
        if len(node) == 2:
            cycle |= (1<<power)
        if center in node: node.remove(center)
        if len(node) == 0:
            cycle |= (1<<power)
            break
        node = modules[node[0]]
        power += 1
    part2 *= cycle
