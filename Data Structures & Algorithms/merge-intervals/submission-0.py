class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)
        res = [intervals.pop(0)]

        while intervals:
            cur = intervals.pop(0)
            last = res[-1]
            if cur[0] > last[-1]:
                res.append(cur)
                continue
            res[-1][-1] = max(res[-1][-1],cur[-1])

        return res
