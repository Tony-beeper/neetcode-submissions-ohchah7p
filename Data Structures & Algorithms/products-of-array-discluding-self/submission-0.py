class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running_prod = 1

        arr = [1] * len(nums)
        for i,x in enumerate(nums):
            arr[i] = running_prod
            running_prod *= x
        # print(arr)
        running_prod = 1
        for i in range(len(nums)-1,-1,-1):
            arr[i] *= running_prod
            running_prod *= nums[i]
            # print(arr[i])
        # arr.reverse()
        return arr