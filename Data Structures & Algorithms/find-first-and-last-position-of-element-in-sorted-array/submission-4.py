from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_ge(val):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= val:
                    right = mid
                else:
                    left = mid + 1
            return left
        found_left = first_ge(target)

        if len(nums) == found_left or nums[found_left]!=target:
            return [-1,-1]
        found_right = first_ge(target+1) -1
        return [found_left, found_right]
