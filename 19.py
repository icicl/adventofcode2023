import aoc

d = aoc.load(19, raw=True)
rules_text = d.split('\n\n')[0].split('\n')
parts_text = d.split('\n\n')[1].split('\n')
rules = {}
for i in rules_text:
    name, rest = i.split('{')
    conds = []
    for j in rest.split(','):
        conds.append(j.split(':'))
    conds[-1] = ['True',conds[-1][0][:-1]]
    rules[name] = conds
parts = []
for part in parts_text:
    parts.append([int(i.split('=')[1]) for i in part[:-1].split(',')])

part1 = 0
for i in parts:
    w = 'in'
    while not w in {'R', 'A'}:
        x,m,a,s = i
        r = rules[w]
        for c,des in r:
            if eval(c):
                w = des
                break
    if w == 'A':
        part1 += sum(i)

queue = [{'loc':'in', 'x':[1,4000], 'm':[1,4000], 'a':[1,4000], 's':[1,4000]}]
part2 = 0
while queue:
    a = queue.pop()
    if a['loc'] == 'R':
        continue
    if a['loc'] == 'A':
        part2 += aoc.pi([a[xmas][1] - a[xmas][0] + 1 for xmas in 'xmas'])
        continue
    rule = rules[a['loc']]
    for cond, dest in rule:
        if cond == 'True':
            a['loc'] = dest
            queue.append(a)
            break
        sign = cond[1]
        idx = cond[0]
        num = int(cond[2:])
        if sign == '<':
            if a[idx][1] < num:
                a['loc'] = dest
                queue.append(a)
                break
            elif a[idx][0] >= num:
                continue
            else:
                b = {xmas:a[xmas] for xmas in 'xmas'}
                b['loc'] = dest
                b[idx] = [a[idx][0], num - 1]
                queue.append(b)
                a[idx] = [num, a[idx][1]]
        elif sign == '>':
            if a[idx][0] > num:
                a['loc'] = dest
                queue.append(a)
                break
            elif a[idx][1] <= num:
                continue
            else:
                b = {xmas:a[xmas] for xmas in 'xmas'}
                b['loc'] = dest
                b[idx] = [num+1, a[idx][1]]
                queue.append(b)
                a[idx] = [a[idx][0], num]
