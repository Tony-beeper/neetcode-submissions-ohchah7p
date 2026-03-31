class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            # = 2
        
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # print("left="+str(left)+"right="+str(right)+"mid="+str(mid))
            #right half sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        if nums[right] == target:
            return right
        return -1
