class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in close_to_open:
                if stk and stk[-1] == close_to_open[ch]:
                    stk.pop(-1)
                else:
                    return False
            
            else:
                stk.append(ch)

        return len(stk) == 0

