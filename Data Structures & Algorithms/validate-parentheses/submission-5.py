class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        paras = {'(':')','{':'}','[':']'}

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            if ch in "])}":
                if not stack:
                    return False
                match = stack.pop(-1)
                if paras[match] != ch:
                    return False
        return True if not stack else False