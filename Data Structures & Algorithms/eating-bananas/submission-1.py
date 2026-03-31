class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles) == 0:
        #     return piles[0] > h
        right = max(piles)
        left = 1
        min_b = max(piles)
        def can_finish(b):
            # if < h, then can finish
            hrs = 0
            for p in piles:
                if p % b == 0:
                    # hrs += (p + b - 1) // b 
                    hrs += p // b 
                else:
                    hrs += p // b + 1
            return hrs <= h
            
            # else can't
        while left < right:
            # if finished goes smaller, if not, goes larger
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        return right