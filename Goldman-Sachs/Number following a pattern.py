class Solution:
    def printMinNumberForPattern(ob,S):
        t = []
        res=""
        for i in range(len(S)+1):
            t.append(i+1)
            if (i==len(S) or S[i]=="I"):
                while (len(t)>0):
                    res+=str(t[-1])
                    t.pop()

        return res
