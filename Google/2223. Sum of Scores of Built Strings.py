class Solution:
    def sumScores(self, A: str) -> int:
        m = len(A)

        def bisect_strs(t):
            lo, hi = 0 , len(t)
            if A[0]!= t[0]:
                return 0
            if t == A[:hi]:
                return hi
            
            while lo < hi:
                mid = (lo+hi) >>1
                if A[:mid+1] == t[:mid+1]:
                    lo = mid +1
                else:
                    hi = mid

            return lo
        res = 0
        for i in range(m):
            res += bisect_strs(A[i:])
        return res
