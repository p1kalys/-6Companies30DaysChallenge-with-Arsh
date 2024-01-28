class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        d = []
        for i in range(len(aliceValues)):
            d.append([aliceValues[i], bobValues[i]])
        d.sort(key = lambda x:x[0]+x[1], reverse = True)
        a = 0
        b=0
        for i in range(len(d)):
            if i%2==0:
                a+=d[i][0]
            else:
                b+=d[i][1]
        if a>b:
            return 1
        elif b>a:
            return -1
        else:
            return 0
