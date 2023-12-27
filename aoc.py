import requests, os, re
from PIL import Image as I
from IPython.display import display
from itertools import product

cookie = "00"
year = "2023"
def load(day, raw=False):
    if not os.path.exists(str(day).zfill(2) + ".txt"):
        r = requests.get("https://adventofcode.com/" + year + "/day/" + str(day) + "/input", headers = {"Cookie": "session=" + cookie})
        if r.status_code != 200:
            print("Input could not be retrieved.")
            return []
        with open(str(day).zfill(2) + ".txt", "w+") as f:
            f.write(inp := r.text)
    else:
        with open(str(day).zfill(2) + ".txt") as f:
            inp = f.read()
    return inp[:-1] if raw else inp[:-1].split('\n')

def loadints(day):
    return [ints(i) for i in load(day)]
def pi(arr):
    res = 1
    for i in arr: res *= i
    return res

def ints(s):
    return [int(i) for i in re.findall('-?\d+',s)]

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __repr__(self):
        return f"({self.start} -> {self.end})"
    def __lt__(self, other):
        return self.start < other.start
    def touch(self, other):
        return not (other.end < self.start or other.start > self.end)
    def union(self, other):
        assert self.touch(other), "cannot take union of two Range objects that do not touch."
        return Range(min(self.start, other.start), max(self.end, other.end))
    def overlap(self, other):
        if not self.touch(other): return None
        return Range(max(self.start, other.start), min(self.end, other.end))
    def merge(self, other):
        assert self.touch(other), "cannot take union of two Range objects that do not touch."
        self.start = min(self.start, other.start)
        self.end = max(self.end, other.end)
    def clip(self, other):
        if not self.touch(other): return None
        self.start = max(self.start, other.start)
        self.end = min(self.end, other.end)
    def mergein(self, q):
        for j in q[::-1]:
            if j.touch(self):
                self.merge(j)
                q.remove(j)
        q.append(self) ## TODO add insort
    def size(self):
        return self.end - self.start + 1

def prime(n):
    if n < 10: return n in {2,3,5,7}
    if n%2 == 0: return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    return True

def factor(n):
    if n <= 0: return []
    f = []
    while n%2 == 0:
        f.append(2)
        n //= 2
    i = 3
    while i*i <= n:
        while n%i == 0:
            f.append(i)
            n //= i
        i += 2
    if n != 1: f.append(n)
    return f

def divisors(n):
    if n <= 0: return [0]
    if n == 1: return [1]
    f = factor(n)
    c = {i:0 for i in f}
    for i in f: c[i] += 1
    s = []
    for i in c:
        s += [[]]
        m = 1
        for _ in range(c[i] + 1):
            s[-1] += [m]
            m *= i
    return set(pi(i) for i in product(*s))

def copy(x):
    return [i for i in x]

def orange(a, b):
    return range(a, b + 1) if a < b else range(b, a + 1)

def xy(z):
    return int(z.real), int(z.imag)

def visualize(data, trace=False, complex=True, scale=1, active=[(0,0,0), (31,31,31)], blank=(255,255,255), save=''):
    nx, xx, ny, xy_ = 1<<31, -(1<<31), 1<<31, -(1<<31)
    for z in data:
        if complex: x,y = xy(z)
        else: x,y=z
        nx = min(x, nx)
        xx = max(x, xx)
        ny = min(y, ny)
        xy_ = max(y, xy_)
    im = I.new('RGB', (xx - nx + 1, xy_ - ny + 1), color=blank)
    il = im.load()
    if trace:
        if complex: px, py = xy(data[-1])
        else: px, py = data[-1]
    for z in data:
        if complex: x,y = xy(z)
        else: x,y=z
        if trace:
            for x_ in orange(x, px):
                for y_ in orange(y, py):
                    il[x_ - nx, y_ - ny] = active[(x_+y_)%len(active)]
            px, py = x, y
        il[x - nx, y - ny] = active[(x+y)%len(active)]
    cnt = 0
    for z in data:
        cnt += 1
        if complex: x,y = xy(z)
        else: x,y=z
    if save: im.save(save + '.png')
    else: display(im.resize((scale*(xx-nx+1), scale*(xy_-ny+1)), resample=I.NEAREST))

def bfs(node, dest, graph, score=0, seen=set()):
    if node == dest:
        yield score

    for p, dist in graph[node]:
        if p in seen:
            continue
        yield from bfs(p, dest, graph, score + dist, seen | {node})

def bfs_track(node, dest, graph, score=0, seen=set(), hist=[]):
    if node == dest:
        yield score, hist

    for p, dist in graph[node]:
        if p in seen:
            continue
        yield from bfs_track(p, dest, graph, score + dist, seen | {node}, hist + [node])


ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "abcdefghijklmnopqrstuvwxyz"
DXY = {(1,0),(-1,0),(0,1),(0,-1)}
DZ = {-1, 1, -1j, 1j}
english_nums = ['zero','one','two','three','four','five','six','seven','eight','nine']