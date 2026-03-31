class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = int((left + right) / 2)
            mid = nums[mid_index]
            if mid > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
            # else:
            #     return mid_index
        if nums[right] == target:
            return right
        return -1