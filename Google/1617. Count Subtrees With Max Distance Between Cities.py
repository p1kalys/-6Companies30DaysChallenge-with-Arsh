class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        d = [[float('inf')]*n for _ in range(n)]
        for i,j in edges:
            d[i-1][j-1] = d[j-1][i-1] = 1
        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][mid] + d[mid][j])
        def f(sub):
            edge = 0
            node = 0
            maxi = 0
            for i in range(n):
                if (sub>>i)&1==0:
                    continue
                node += 1
                for j in range(i+1,n):
                    if (sub>>j)&1 == 0:
                        continue
                    edge += d[i][j]==1
                    maxi = max(maxi, d[i][j])
            if edge!=node-1:
                return 0
            else:
                return maxi

        res = [0]*(n-1)
        for i in range(1, 2**n):
            temp = f(i)
            if temp>0:
                res[temp-1]+=1
        return res
