class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        elif len(nums) == 1:
            
            return [0,0] if target == nums[0] else [-1,-1]
        # find left
        left = 0
        right = len(nums) - 1
        found_left = -1
        found_right = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid - 1 < 0 or nums[mid-1] != target:
                    found_left = mid
                    break
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            # print(mid)
        left = 0
        right = len(nums) - 1
        # print("hi")

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid + 1 >= len(nums) or nums[mid+1] != target:
                    found_right = mid
                    break
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = mid + 1

        if found_right == -1 and found_left != -1:
            found_right = found_left
        elif found_left == -1 and found_right != -1:
            found_left = found_right
        return [found_left,found_right]





        # find right