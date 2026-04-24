class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for x in nums:
            if x in a:
                return True
            a.add(x)
        return False