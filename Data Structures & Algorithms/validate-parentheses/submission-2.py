class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for i in s:
            # push if (, {, [
            # pop if ...

            if i in "({[":
                stk.append(i)
            elif len(stk)>0:
                if (stk[-1] == '(' and i == ')') or (stk[-1] == '{' and i == '}') or (stk[-1]=='[' and i==']'):
                    stk.pop(-1)
                    # print('io')
                else:
                    return False
            else:
                return False
        if len(stk) == 0:
            print(stk)
            return True

        return False
