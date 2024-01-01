class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        com_mul = math.lcm(divisor1, divisor2)

        def isPossible(num):
            c1 = num - (num//divisor1)
            c2 = num - (num//divisor2)

            total = num - (num//com_mul)

            return c1>=uniqueCnt1 and c2>=uniqueCnt2 and total>=uniqueCnt1+uniqueCnt2

        i = 0
        j = 2**31 - 1
        
        while i < j:
            m = (i+j)//2
            if isPossible(m):
                j = m
            else:
                i = m+1
        return i