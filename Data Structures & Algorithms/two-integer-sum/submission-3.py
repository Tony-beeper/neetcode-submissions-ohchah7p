class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a ={}

        for i,num in enumerate(nums):
            complement = target-num
            if complement in a:
                return [a[complement], i]
            a[num] = i
        return [-1,-1]

