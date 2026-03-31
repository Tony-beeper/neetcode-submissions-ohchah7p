class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [0,0]
        for i, num in enumerate(nums):
        # for i in range(len(nums)):
            cur_max = max(arr[i-1+2],arr[i-2+2]+num)
            arr.append(cur_max)
        # print(arr)
        return arr[-1]
