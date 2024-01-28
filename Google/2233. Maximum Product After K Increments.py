import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k>0:
            n = heapq.heappop(nums)
            heapq.heappush(nums, n+1)
            k-=1
        res = 1
        mod = 10**9 + 7
        for i in nums:
            res *= i
            res%=mod
        return res
