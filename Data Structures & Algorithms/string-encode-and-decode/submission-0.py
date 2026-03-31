class Solution:

    def encode(self, strs: List[str]) -> str:
        # apply a number + a pound # before the string
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        return res
    def decode(self, s: str) -> List[str]:
        # while not the end of s
        # search for number and first pound
        # append to list

        start = 0
        res = []
        while start < len(s):
            # check number of digits for
            x = start
            while s[x] != '#':
                x+=1
                # print(s[x])
            # start at start, end at x
            num = ""
            for i in range(start, x):
                num += s[i]
            num = int(num)
            #get that str
            cur_str = ""
            for i in range(num):
                cur_str += s[i+x+1]
            res.append(cur_str)
            start = x + num + 1
        return res



