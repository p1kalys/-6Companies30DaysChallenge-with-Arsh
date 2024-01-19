class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 2*n
        p = defaultdict(set)
        for i,j in reservedSeats:
            if j==4 or j==5:
                p[i].add(0)
                p[i].add(1)
            if j==6 or j==7:
                p[i].add(1)
                p[i].add(2)
            if j==8 or j==9:
                p[i].add(2)
            if j==2 or j==3:
                p[i].add(0)
        
        for i in p:
            if len(p[i]) >   = 3:
                res-=2
            else:
                res-=1
        return res
