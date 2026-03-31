class Solution:
    def decodeString(self, s: str) -> str:
        
        
        def bracket(i):

            inner_str = ""
            repeats = 0
            i+=1
            while i < len(s):
                ch = s[i]
                if s[i].isalpha():
                    inner_str += ch
                elif s[i].isdigit():
                    repeats *= 10
                    repeats += int(s[i])
                elif s[i] == '[':
                    i, returned_str = bracket(i)
                    inner_str += repeats * returned_str
                    repeats = 0
                    # i+=1
                elif s[i] == ']':
                    return i, inner_str
                i+=1
            return i, inner_str

        res = ""
        reps = 0
        i = 0
        while i < len(s):
            ch = s[i]
            if s[i].isalpha():
                res += ch
            elif s[i].isdigit():
                reps *= 10
                reps += int(s[i])
            elif s[i] == '[':
                i, cur_str = bracket(i)
                res += reps * cur_str
                reps = 0

            i+=1

        return res