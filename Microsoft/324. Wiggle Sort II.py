class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        array = sorted(nums)
        for i in range(1,n,2):
            nums[i] = array.pop()
        for i in range(0,n,2):
            nums[i] = array.pop()
