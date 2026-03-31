class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq= {}
        most_common = 0

        left = 0
        max_len = 0
        for i,right in enumerate(s):
            freq[right] = freq.get(right,0) + 1
            most_common = max(most_common,freq[right])

            while (i - left + 1) - most_common > k:
                left_char = s[left]
                freq[left_char] -= 1
                left+=1

            max_len = max(max_len, i-left+1)
        return max_len