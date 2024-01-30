class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dir = [[-1,0],[0,1],[1,0],[0,-1]]

        def dfs(r,c,visit):
            if r<0 or c<0 or c>=m or r>=n or (r,c) in visit or grid[r][c]==0:
                return 
            visit.add((r,c))
            for dr, dc in dir:
                dfs(r+dr, c+dc, visit)
        def f():
            islands = 0
            visited = set()
            for r in range(n):
                for c in range(m):
                    if grid[r][c]==1 and (r,c) not in visited:
                        islands += 1
                        dfs(r,c,visited)
            return islands

        islands = f()
        if islands!=1:
            return 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    islands = f()
                    if islands!=1:
                        return 1
                    grid[r][c] = 1
        return 2
