class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left:
            maxL = -1 
        else:
            maxL = max(left)

        if not right:
            minR = 10001
        else:
            minR = min(right)

        return max(maxL, n - minR)
            
