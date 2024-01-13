class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        rows, cols = len(nums1), len(nums2)
        matrix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        answer = 0

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if nums1[row] == nums2[col]:
                    matrix[row][col] = 1 + matrix[row + 1][col + 1]
                    answer = max(answer, matrix[row][col])

        return answer
