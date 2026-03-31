class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0

        cur_num = 0
        op = '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                cur_num *= 10 
                cur_num += int(ch)
            
            if ch in "+-*/" or i == len(s) -1:
                if op == "+":
                    stack.append(cur_num)
                elif op == "-":
                    stack.append(-cur_num)
                elif op == "*":
                    prev = stack.pop()
                    stack.append(cur_num * prev)
                elif op == "/":
                    prev = stack.pop()
                    stack.append(int(prev / cur_num))
                op = ch
                cur_num = 0
        return sum(stack)


