class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:

        #Make a set of sorted startWords
        start = set([''.join(sorted(item)) for item in startWords])

        count = 0
        for item in targetWords:

            #Sort letters for each targetWord to match them with startWords
            word = ''.join(sorted(item))

            #Remove letters one by one to see if any of the startWords match
            n = len(item)
            for i in range(n):
                if word[:i] + word[i+1:] in start:
                    count += 1
                    break

        return count
