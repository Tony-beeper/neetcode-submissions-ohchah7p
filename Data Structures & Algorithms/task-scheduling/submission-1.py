import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)
        q = deque()
        time = 0
        while maxheap or q:
          time += 1
          if maxheap:
            count = maxheap.pop(0) + 1
            if count:
              q.append((count, time + n))
          if q and q[0][1] == time:
            heapq.heappush( maxheap,q.popleft()[0])

        return time