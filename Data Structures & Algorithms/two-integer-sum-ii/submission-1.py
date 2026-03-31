class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in d:
                return [d[complement] + 1, i + 1]
            d[num] = i
        return []
