class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        f = min(x,y)
        g = max(x,y)
        return f*2 + (f+1 if g>f else f)*2 + z*2
