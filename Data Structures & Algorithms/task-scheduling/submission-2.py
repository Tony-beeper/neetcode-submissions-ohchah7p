class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        coutns = Counter(tasks)

        maxheap = [-c for c in coutns.values()]
        heapq.heapify(maxheap)

        q = deque()

        time = 0

        while maxheap or q:
          time += 1
          if maxheap:
            count = heapq.heappop(maxheap) + 1
            if count:
              q.append((time+n, count))
          if q and q[0][0] == time:
            task = q.popleft()
            heapq.heappush(maxheap,task[1])
            # tasks.append(task)
        return time
            