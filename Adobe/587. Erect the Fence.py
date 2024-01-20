class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def comp(z1, z2, z3):
            x1, y1 = z1
            x2, y2 = z2
            x3, y3 = z3
            return (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)

        trees.sort(key=lambda x: (x[0], x[1]))

        upper = []
        lower = []

        for point in trees:
            while len(lower) > 1 and comp(lower[-2], lower[-1], point) > 0:
                lower.pop()
            while len(upper) > 1 and comp(upper[-2], upper[-1], point) < 0:
                upper.pop()
            upper.append(point)
            lower.append(point)
        for i in lower:
            if i not in upper:
                upper.append(i)
        return upper
