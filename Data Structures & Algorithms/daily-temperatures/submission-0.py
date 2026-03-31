class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        wait = []
        for i,temp in enumerate(temperatures):
            while wait and wait[-1][1] < temp:
                tup = wait.pop(-1)
                res[tup[0]] = i - tup[0]
            wait.append((i,temp))



        return res
