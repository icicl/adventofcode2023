import aoc

d = aoc.load(1)
 
v = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

part1 = 0
part2 = 0

for i in d:
    i = str(i)
    d1, d2 = [], []
    while i:
        for k in v:
            if len(k) <= len(i):
                if i[:len(k)] == k:
                    d2 += [v[k]]
                    if len(k) == 1: d1 += [v[k]]
                    break
        i = i[1:]
    part1 += d1[0]*10+d1[-1]
    part2 += d2[0]*10+d2[-1]
