class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            a = [0 for _ in range(26)]
            for ch in s:
                a[ord(ch)-ord('a')] += 1
            a = "/".join(map(str,a))
            # print(a)

            groups[a].append(s)
        res = []
        for key in groups:
            res.append(groups[key])
        return res

