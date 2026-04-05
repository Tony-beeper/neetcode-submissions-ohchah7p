class Solution:
    def decodeString(self, s: str) -> str:
        

        def parse(i):
            
            counter = 0
            res = ""
            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    counter = counter * 10 + int(ch)
                elif ch == "[":
                    i, returned = parse(i+1)
                    # print(returned)
                    res += counter * returned
                    counter = 0
                elif ch == "]":
                    # print(res)
                    return i, res
                else:
                    res += ch

                i += 1
            return i, res
        return parse(0)[1]
                


        