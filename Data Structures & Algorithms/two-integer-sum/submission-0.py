class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i,num in enumerate(nums):
            
            if num in a:
                return [a[num],i]
            complement = target - num
            a[complement] = i
        # print(a)
        return [0,0]
