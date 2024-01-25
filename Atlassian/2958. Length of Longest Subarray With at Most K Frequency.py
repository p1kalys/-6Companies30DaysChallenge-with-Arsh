class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)

        s = 0
        e = 0
        res = 0

        while s < len(nums) and e < len(nums):
            d[nums[e]] += 1
            if d[nums[e]] <= k:
                res = max(res, e-s+1)
            else:
                while d[nums[e]] > k:
                    d[nums[s]] -= 1
                    s += 1
            e += 1
        return res
