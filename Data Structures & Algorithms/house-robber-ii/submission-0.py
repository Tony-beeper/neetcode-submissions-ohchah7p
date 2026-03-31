class Solution:
    def rob(self, nums: List[int]) -> int:
        
        arr = [0,0,0]
        arr2 = [0,0,nums[0]]

        for i in range(1,len(nums)):
            if i == len(nums) - 1:
                cur_max = max(arr[i-1+2],arr[i-2+2] + nums[i])
                arr.append(cur_max)
                arr2.append(arr2[-1])
                break
            cur_max = max(arr[i-1+2],arr[i-2+2] + nums[i])
            arr.append(cur_max)
            cur_max = max(arr2[i-1+2],arr2[i-2+2] + nums[i])
            arr2.append(cur_max)


        return max(arr[-1],arr2[-1])