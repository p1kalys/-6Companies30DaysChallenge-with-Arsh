class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = [[0]*len(img[0]) for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[i])):
                res = 0
                count = 0
                for x in [i-1,i,i+1]:
                    for y in [j-1,j,j+1]:
                        if 0<=x<len(img) and 0<=y<len(img[0]):
                            res+=img[x][y]
                            count+=1
                ans[i][j] = res//count
        return ans
