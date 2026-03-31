class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse=True)

        times = []

        for (pos, speed) in cars:
            time = (target-pos) / speed

            times.append(time)
            if len(times) >= 2 and times[-1] <= times[-2]:
                times.pop(-1)
        return len(times)