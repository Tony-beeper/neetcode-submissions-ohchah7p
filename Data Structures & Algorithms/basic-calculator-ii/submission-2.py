class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = '+'
        cur_num = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                cur_num *= 10
                cur_num += int(ch)
            
            if ch in "+-*/" or len(s) - 1 == i:
                if op == '+':
                    stack.append(cur_num)
                elif op == '-':
                    stack.append(-cur_num)
                elif op == '*':
                    stack.append(cur_num * stack.pop())
                elif op == '/':
                    stack.append(int(stack.pop() /cur_num))


                cur_num = 0
                op = ch
        return sum(stack)
