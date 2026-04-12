import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) == 1:
        #     return 0 if target in nums else -1
        left = 0
        right = len(nums) - 1

        while nums[left] > nums[right]:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        idx1 = bisect.bisect_left(nums[left:], target)
        idx2 = bisect.bisect_left(nums[:left], target)
        if idx1 < len(nums[left:]) and nums[left:][idx1] == target:
            return left + idx1
        if idx2 < len(nums[:left]) and nums[idx2] == target:
            return idx2
        return -1
