class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for x,y,h in buildings:
            points.append([x,-h,0])
            points.append([y,h,1])
        points.sort()
        res = []
        pq = [0]
        for x,h,f in points:
            if f==0:
                heapq.heappush(pq,h)
            else:
                pq.remove(-h)
                heapq.heapify(pq)
            cur = -pq[0]
            if not res or res[-1][1]!=cur:
                res.append([x,cur])
        return res
