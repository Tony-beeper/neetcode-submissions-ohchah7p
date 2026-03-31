class Solution:
    def decodeString(self, s: str) -> str:
        # def push():


        def parse(i):
            res = ""
            cur_num = 0
            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    cur_num *= 10
                    cur_num += int(ch)
                elif ch.isalpha():
                    res += ch
                elif ch == ']':
                    return i, res
                elif ch == '[':
                    i, inner = parse(i+1)
                    # for _ in range(cur_num):
                    res += cur_num * inner
                    cur_num = 0
                i+=1
            return i, res
        

        return parse(0)[1]
