class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = []
        d = defaultdict(list)
        for i,j in matches:
            d[i].append(0)
            d[j].append(1)
        no_loss = []
        one_loss = []
        for i,j in d.items():
            if sum(j)==0:
                no_loss.append(i)
            elif sum(j)==1:
                one_loss.append(i)
        no_loss.sort()
        one_loss.sort()
        return [no_loss,one_loss]
