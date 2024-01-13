class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f0 = sum([i*num for i,num in enumerate(nums)])
        total, size = sum(nums), len(nums)
        max_f, prev_f = f0, f0
        for i in range(size-1,0,-1):
            num = nums[i]
            nextf = prev_f + total - size*(num)
            max_f = max(max_f,nextf)    
            prev_f = nextf
        return max_f
