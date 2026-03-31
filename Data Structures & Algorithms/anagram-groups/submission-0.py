class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        b = defaultdict(list)

        for i, x in enumerate(strs):
            arr = [0]*26
            for s in x:
                pos = ord(s) - ord('a')
                arr[pos] += 1
            arr = tuple(arr)
            b[arr].append(x)
        return list(b.values())
