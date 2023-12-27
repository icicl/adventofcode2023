import aoc

def pr(i):
    id_ = i.split(':')[0].split(' ')[-1]
    vv = []
    for j in i.split(': ')[1].split('; '):
        v = {'red':-1,'green':-1,'blue':-1}
        for k in j.split(', '):
            v[k.split(' ')[-1]] = int(k.split(' ')[0])
        vv += [v]
    return [int(id_)] + vv

d = aoc.load(2)
d = [pr(i) for i in d]

m = [[max(j[k] for j in i[1:]) for k in ['red','green','blue']] for i in d]

part1 = sum(i[0] for i,j in zip(d,m) if all(j[n] <= 12+n for n in range(3)))
part2 = sum(aoc.pi(i) for i in m)

