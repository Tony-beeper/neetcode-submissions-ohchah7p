class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.split(" ")
        def is_ascii(s):
            return all(ord(c) < 128 for c in s)

        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        # print(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1
        return True