class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        res = 0
        for word in words:
            for j in range(1,len(word)):
                s.discard(word[j:])
        for i in s:
            res += len(i) + 1
        return res
