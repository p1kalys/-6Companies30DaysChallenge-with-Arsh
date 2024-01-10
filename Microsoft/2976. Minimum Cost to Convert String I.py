class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        d = defaultdict(dict)
        src = set(original) | set(source) 
        trg = set(target) | set(changed)

        comb = src & trg

        for c1 in src:
            for c2 in trg:
                d[c1][c2] = inf if c1!=c2 else 0

        for i,j,k in zip(original, changed, cost):
            d[i][j] = min(d[i][j], k)

        for k in comb:
            for i in src:
                for j in trg:
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        ans = 0
        
        for s,t in zip(source, target):
            ans += d[s][t]

        if ans < inf:
            return ans
        else:
            return -1
