class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        # left max > right max, and next one is smaller, collect the right difference, move next
        # vice versa

        # find first indices that available both side

        left_max = 0
        right_max = len(height) - 1
        while height[left_max] and left_max < len(height) == 0:
            left_max += 1

        while height[right_max] and right_max < len(height )== 0:
            right_max -= 1

        left = left_max
        right =right_max
        while left < right:
            if height[left_max] > height[right_max]:
                # cur_water = min(height[left_max], height[right_max]) - height[right]
                cur_water = max(0,height[right_max]-height[right-1])
                right -= 1
                if height[right] > height[right_max]:
                    right_max = right
            else:
                cur_water = min(height[left_max], height[right_max]) - height[left]
                left += 1
                if height[left] > height[left_max]:
                    left_max = left
            total_water += cur_water
        return total_water






