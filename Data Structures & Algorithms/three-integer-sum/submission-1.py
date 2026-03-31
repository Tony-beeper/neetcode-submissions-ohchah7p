class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            
            if i > 0 and nums[i] == nums[i-1]:
                # print("hi")
                # print(i)
                # print(nums[i])
                # print(nums[i-1])
                continue
            
            left = i + 1
            right = len(nums) - 1
            # print()
            # print(i)
            while left < right:
                # print("hi")
                # print(left)
                # print(right)
                # print("hi")
                summ = nums[left] + nums[right] + nums[i]
                # print(summ)
                if summ == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif summ > 0:
                    right -=1
                else:
                    left +=1
                # left += 1
                # right -= 1
            
        return res