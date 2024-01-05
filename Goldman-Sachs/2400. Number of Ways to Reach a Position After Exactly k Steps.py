class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 10**9 + 7
        @cache
        def f(s,e,k):
            if k==0:
                if s==e:
                    return 1
                return 0
            return (f(s-1,e,k-1)%mod + f(s+1,e,k-1)%mod)%mod
        return f(startPos, endPos,k)%mod
