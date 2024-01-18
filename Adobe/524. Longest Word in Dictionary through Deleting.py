class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def f(a,b):
            j = 0
            for i in range(len(a)):
                if a[i]==b[j]:
                    j+=1
                if j==len(b):
                    return True
            return False
        dictionary.sort(key = lambda x:(-len(x),x))
        for c in dictionary:
            if f(s,c):
                return c
        return ""
