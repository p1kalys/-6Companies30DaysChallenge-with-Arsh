class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = [[10001]*n for _ in range(n)]

        for i,j,k in edges:
            d[i][j] = k
            d[j][i] = k

        for k in range(n):
            d[k][k] = 0
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        countcity = n
        citynum = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if d[i][j] <= distanceThreshold:
                    count+=1
            if count <= countcity:
                countcity = count
                citynum = i
        
        return citynum
