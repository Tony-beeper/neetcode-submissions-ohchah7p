class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        bag = set(nums)
        biggest = max(nums)
        counter = 0
        res = 0
        for x in bag:
            if x-1 not in bag:
                cur = x
                while cur in bag:
                    counter+=1
                    cur +=1
                res = max(res,counter)

            counter = 0
        return res
