class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        # print(target)
        if total % 2 == 1:
            # print("hi")
            return False

        possible = {0}

        
        for num in nums:
            next_possible = set(possible)
            for p in possible:
                if p + num == target:
                    return True
                if p + num < target:
                    next_possible.add(p+num)
            possible = next_possible
        print(possible)
        return target in possible



