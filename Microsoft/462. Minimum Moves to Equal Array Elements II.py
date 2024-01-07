class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n=len(nums)
        cmp = nums[n//2]
        for i in range(n):
            res+= abs(cmp-nums[i])
        return res
