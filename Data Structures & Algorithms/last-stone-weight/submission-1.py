import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        # print(heap)
        heapq.heapify(heap)
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            if a == b:
                continue
            else:
                heapq.heappush(heap, -abs(a-b))

        return -heap[0] if len(heap) == 1 else 0