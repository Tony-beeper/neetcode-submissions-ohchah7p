class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]]+=1
            else:
                hash_map[s[i]] = 1
        for i in range(len(t)):
            if t[i] in hash_map and hash_map[t[i]]!=0:
                hash_map[t[i]]-=1
            else:
                return False
        for v in hash_map.values():
            if v != 0:
                return False
        return True

