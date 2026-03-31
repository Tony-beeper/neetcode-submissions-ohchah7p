class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b = {}
        for num in nums:
            b[num] = b.get(num,0) + 1
        buckets = [[] for _ in range(len(nums)+1)] 
        # print(buckets)
        for key in b:
            buckets[b[key]].append(key)
        buckets.reverse()
        res = []
        for bucket in buckets:
            for element in bucket:
                res.append(element)
                if len(res) == k:
                    return res
        return res

