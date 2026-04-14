class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, remaining):

            if remaining == 0:
                result.append(list(current))
                return

            # for i, num in enumerate(nums[start:]):
            for i in range(start, len(nums)):
                if remaining - nums[i] >= 0:
                    current.append(nums[i])
                    backtrack(i, current, remaining - nums[i])
                    current.pop()


        
        backtrack(0, [], target)
        return result