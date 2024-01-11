class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        res = []
        dp = [1]*len(nums)
        temp = 0
        index = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i]%nums[j]==0):
                    dp[i] = max(dp[i],dp[j]+1)
                    if dp[i] > temp:
                        temp = dp[i]
                        index = i
        res.append(nums[index])
        temp-=1
        for i in range(index-1,-1,-1):
            if dp[i] == temp and res[-1]%nums[i]==0:
                res.append(nums[i])
                temp-=1
        return res
