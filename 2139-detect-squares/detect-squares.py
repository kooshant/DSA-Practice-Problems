class DetectSquares:

    def __init__(self):
        #Initialize self.pts = []
        self.pts = []
        #Initialize self.ptsCount = defaultdict(int)
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        #Append point to self.pts
        self.pts.append(point)
        #Update self.ptsCount[tuple(point)] += 1
        self.ptsCount[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        #Initialize output variable res to 0
        res = 0
        #Initialize px, py to values from point
        px, py = point

        #Iterate for x, y in self.pts
        for x, y in self.pts:
            #Check if(abs(py - y) != abs(px - x) or x == px or y == py). This checks if the diagonal points can't be of a square (difference in length and height is different, should be same for squares) and if they aren't the same point
            if(abs(py - y) != abs(px - x) or x == px or y == py):
                #continue
                continue
            #Update res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]. This works because if theres duplicate points it will reflect on that formula
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        
        #return res
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)