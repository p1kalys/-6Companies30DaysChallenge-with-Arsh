class Solution:
    def f(self, i, n, k, temp, res):
        if len(temp)> k or sum(temp) > n:
            return
        if len(temp)==k and sum(temp)==n:
            res.append(temp)
            return
        for j in range(i,10):
            self.f(j+1,n, k, temp+[j],res)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        temp = []
        self.f(1,n,k,temp,res)
        return res
