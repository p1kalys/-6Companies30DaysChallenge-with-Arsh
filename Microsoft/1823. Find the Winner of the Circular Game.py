class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a = []
        for i in range(1,n+1):
            a.append(i)
        i=0
        while len(a)>1:
            i+=k-1
            if i < len(a):
                del a[i] 
            else:
                i%=len(a)
                del a[i]
        return a[0]
