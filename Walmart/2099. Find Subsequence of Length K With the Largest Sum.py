class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        temp = []
        for i in range(n):
            temp.append([nums[i],i])
        temp.sort(key = lambda x:x[0])

        temp = temp[n-k:]

        temp.sort(key = lambda x:x[1])
        res = []
        for i in temp:
            res.append(i[0])
        return res
