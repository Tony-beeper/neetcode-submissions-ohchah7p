class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for x in nums[1:]:
            candidates = (x, x * cur_max, x * cur_min)
            cur_max = max(candidates)
            cur_min = min(candidates)
            ans = max(ans, cur_max)

        return ans
