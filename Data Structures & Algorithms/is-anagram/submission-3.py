class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0 for _ in range(26)]
        b = [0 for _ in range(26)]

        for ch in s:
            a[ord(ch) - ord('a')] += 1
        for ch in t:
            b[ord(ch) - ord('a')] += 1

        return True if a == b else False
            