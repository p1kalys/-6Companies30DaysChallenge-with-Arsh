class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        sq = {4,8,9,12,16,18,20,24,25,27,28}
        def gcd(a,b):
            while b!=0:
                a,b = b, a%b
            return a
        d = {}
        for i in nums:
            if i in sq:
                continue
            temp = dict(d)
            for k in d.keys():
                if gcd(k,i) == 1:
                    cur = k*i
                    if cur in temp:
                        temp[cur] += d[k]
                    else:
                        temp[cur] = d[k]
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
            d = temp
        return sum([d[k] for k in d.keys()]) % (10**9 +7)
