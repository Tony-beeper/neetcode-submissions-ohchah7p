import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        res = -1
        # nums = [-n for n in nums]
        # print(nums)'
        x = len(nums) - k + 1
        for i in range(x):
            # print('h')
            res = heapq.heappop(nums)
        return res