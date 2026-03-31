import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []

        for p in points:
            x = p[0]
            y= p[1]

            dis = math.sqrt((x**2 +y**2))
            # print(p)
            # print(dis)
            # print(x)
            # print(y)
            heapq.heappush(pts, (dis,p))
        # print(pts)
        res = []
        for i in range(k):
            res.append(heapq.heappop(pts)[1])
        return res
        