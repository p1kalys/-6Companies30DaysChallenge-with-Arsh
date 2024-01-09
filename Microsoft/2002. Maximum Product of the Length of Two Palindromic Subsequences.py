class Solution:
    def maxProduct(self, s: str) -> int:
        ans = 0

        @cache
        def dp(s):
            if len(s)==0:
                return 0
            if len(s)==1:
                return 1
            else:
                if s[0]==s[-1]:
                    return dp(s[1:-1]) + 2
                else:
                    return max(dp(s[1:]), dp(s[:-1]))

        def generate(s1,s2,ind):
            if ind == len(s):
                nonlocal ans
                ans = max(ans, dp(s1) * dp(s2))
                return

            generate(s1 + s[ind], s2, ind+1)
            generate(s1, s2 + s[ind], ind+1)

        generate("","",0)
        return ans
