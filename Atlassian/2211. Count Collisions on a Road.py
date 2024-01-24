class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        res = 0
        i = 0
        while i<n and directions[i]=='L':
            i += 1
            res += 1
        i = n-1
        while i>=0 and directions[i]=='R':
            i -= 1
            res += 1
        res += directions.count('S')
        return n - res
