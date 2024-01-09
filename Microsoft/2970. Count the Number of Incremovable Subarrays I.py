class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1,n+1):
                sub = nums[i:j]
                left = nums[:i]
                right = nums[j:]
                remain = left+right

                if sorted(remain) == remain and len(remain) == len(list(set(remain))):
                    count+=1
        return count
