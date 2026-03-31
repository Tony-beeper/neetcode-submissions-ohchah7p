class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = sorted(list(zip(position,speed)),reverse=True)
        # print(cars)

        for (pos,speed) in cars:
            time = (target-pos) / speed

            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop(-1)
        return len(stack)
