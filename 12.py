import aoc
from functools import cache
d = aoc.load(12)

def process(i, repeat=1):
    cond = ((i[0] + '?')*repeat)
    nums = eval(f'[{((i[1]+",")*repeat)[:-1]}]')
    @cache
    def p2(cur, lp):
        res = 0
        if lp == len(nums):
            return not '#' in cond[cur + nums[lp-1]:]
        if '#' in cond[cur + nums[lp-1] if cur != -1 else 0:(cur + nums[lp-1] + 1) if cur != -1 else 0]: return 0
        for p in range((cur + nums[lp-1] + 1) if cur != -1 else 0, len(cond) - sum(nums[lp:]) - (len(nums) - lp) + 1):
            if cond[p-1] == '#': break
            if not '.' in cond[p:p+nums[lp]]:
                res += p2(p, lp + 1)
        return res
    return p2(-1, 0)

part1 = (sum(process(i.split())for i in d))
part2 = (sum(process(i.split(),5)for i in d))
