class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        global_max = max(cur_max, cur_min)

        for n in nums[1:]:
            candidates = (n,cur_max * n, cur_min * n)
            cur_max = max(candidates)
            cur_min = min(candidates)
            global_max = max(global_max, cur_max)

        return global_max
