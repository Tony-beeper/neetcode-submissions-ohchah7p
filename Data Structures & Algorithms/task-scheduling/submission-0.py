class Solution:
    def leastInterval(self, tasks, n):
       count = Counter(tasks)
       max_heap = [-c for c in count.values()]
       heapq.heapify(max_heap)
       queue = deque()
       time = 0
       while max_heap or queue:
          time += 1
          if max_heap:
            count = heapq.heappop(max_heap) + 1
            if count:
                queue.append((count, time + n))
          if queue:
            if queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        


       return time