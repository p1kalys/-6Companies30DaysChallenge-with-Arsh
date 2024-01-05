class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        if delay >=forget:
            return 1
        mod = 10**9 + 7
        dp = [0]*(n)
        dp[0]=1
        user = 0
        for i in range( 1,n):
            if (i-delay)>=0:
                user += dp[i-delay]
            if i-forget>=0:
                user -= dp[i-forget]
            dp[i] = user%mod
        res = sum(dp[-forget:])%mod
        return res
