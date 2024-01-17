class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, x: int, y: int) -> List[List[int]]:
        res = []
        for i in range(rows):
            for j in range(cols):
                s = abs(x-i) + abs(y-j)
                res.append([s,[i,j]])
        res = [x for i,x in sorted(res)]
        return res
