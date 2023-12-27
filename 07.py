import aoc

d = [[i[:5], int(i[6:])] for i in aoc.load(7)]

def score(s):
    c = sorted({i:s.count(i) for i in s}.values())
    return [[1,1,1,1,1],[1,1,1,2],[1,2,2],[1,1,3],[2,3],[1,4],[5]].index(c)

def score2(s):
    return max(score(s.replace('J',i))for i in '23456789TQKA')

def srt(s):
    sc = score(s)*13**5
    for i in range(5):
        sc += '23456789TJQKA'.index(s[i])*(13**(4-i))
    return sc

def srt2(s):
    sc = score2(s)*13**5
    for i in range(5):
        sc += 'J23456789TQKA'.index(s[i])*(13**(4-i))
    return sc

d = sorted(d, key=lambda x:srt(str(x[0])))
part1 = 0
for i in range(len(d)):
    part1 += (i+1)*d[i][1]

d = sorted(d, key=lambda x:srt2(str(x[0])))
part2 = 0
for i in range(len(d)):
    part2 += (i+1)*d[i][1]
