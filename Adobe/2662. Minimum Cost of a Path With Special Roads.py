class Solution:
    def minimumCost(self, start: List[int], target: List[int],
                          specialRoads: List[List[int]]) -> int:

        dist = lambda x, y: abs(x[0]-y[0])+abs(x[1]-y[1])

        specialRoads = tuple(((x1,y1),(x2,y2),cost) for x1,y1,x2,y2,cost
                               in specialRoads if dist((x1,y1),(x2,y2)) > cost)
        
        mn = dist(start, target)
        seen, heap = set(), [(0,tuple(start))]

        
        while heap:
            cost, pos = heappop(heap)

            if pos in seen or cost > mn: continue

            mn = min(mn, cost + dist(pos, target))        #  <-- (a)
            seen.add(pos)

            for rdBeg, rdEnd, roadCost in specialRoads:   #  <-- (b)
                heappush(heap, (cost + roadCost + dist(pos,rdBeg), rdEnd))
                
        return mn
