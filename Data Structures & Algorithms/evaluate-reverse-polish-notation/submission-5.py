class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = []
        nums = []
        res = 0
        # res = 0
        # first_op = True
        # cur = 0
        for i, s in enumerate(tokens):
            if s not in {"+", "-", "*", "/"}:
                # print("hi")
                nums.append(int(s))
                # print(s)
            else:
                b= nums.pop(-1)
                a= nums.pop(-1)
                
                # first op needs to pop 2
                # res just pop one
                if s == '+':
                    res = a + b
                elif s == '-':
                    res = a - b
                elif s == '*':
                    res = a * b
                elif s == '/':
                    res = int(a / b)
                nums.append(res)
        return nums[0]

