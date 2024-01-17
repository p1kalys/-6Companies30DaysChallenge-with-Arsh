class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        dp = [[-1]*(1<<n + 1) for _ in range(n+1)]

        def f(prev, mask,count):
            if count==n:
                return 1
            if dp[prev+1][mask]!=-1:
                return dp[prev+1][mask]
            res = 0
            for i in range(n):
                if mask & (1<<i):
                    continue
                if prev == -1 or nums[i]%nums[prev]==0 or nums[prev]%nums[i]==0:
                    res += f(i, mask | 1<<i, count + 1)
                    res%=MOD
            dp[prev+1][mask] = res
            return res
        return f(-1,0,0)
