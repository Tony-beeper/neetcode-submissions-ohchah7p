class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0

        max_window_size = 0

        dic = {}
        for i,s in enumerate(s):
            # if window_start > i:
            #     continue
            # print(i)
            # print(s)
            # print(dic)
            if dic.get(s) != None:
                # print(s)
                # print(i)
                prev_pos = dic[s]
                # print(prev_pos)
                if prev_pos >= window_start:
                    # new window start need to be +1
                    # print(s)
                    window_start = prev_pos + 1
            #         print("hi")
            #         print(max_window_size)
            # print(s)
            # print(i)
            
            dic[s] = i # last seen
            # print(dic)
            max_window_size = max(max_window_size, i - window_start+1)
            # print(max_window_size)
        return max_window_size
