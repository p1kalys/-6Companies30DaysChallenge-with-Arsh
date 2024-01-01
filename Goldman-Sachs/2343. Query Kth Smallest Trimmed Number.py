class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        for query in queries:
            temp = []
            trim = query[1]
            k = query[0]
            for j in range(len(nums)):
                if trim >= len(nums[j]):
                    num = int(nums[j])
                else:
                    num = int(nums[j][-trim:])
                temp.append((num, j))

            temp.sort()
            res.append(temp[k-1][1])

        return res
