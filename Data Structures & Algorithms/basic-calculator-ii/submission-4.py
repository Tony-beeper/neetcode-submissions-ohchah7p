class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip(' ')
        print(s)
        stack = []

        op = "+"

        cur_num = 0
        for i,ch in enumerate(s):
            if ch == ' ':
                continue
            if ch.isdigit():
                cur_num *= 10
                cur_num += int(ch)
            
            if ch in "+-*/" or i == len(s) - 1:
                if op == '+':
                    stack.append(cur_num)
                elif op == '-':
                    stack.append(-cur_num)
                elif op == '*':
                    stack.append(stack.pop() * cur_num)
                elif op == '/':
                    stack.append(int(stack.pop() / cur_num))
                    # print("hi")
                cur_num = 0
                op = ch
            # print(stack)

        return sum(stack)