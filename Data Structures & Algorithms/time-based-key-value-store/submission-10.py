class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        cur_map = self.timemap[key]
        left = 0
        right = len(cur_map)

        while left < right:
            mid = (left + right) // 2
            if cur_map[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        left -= 1
        print(cur_map)
        print(left)
        if 0 <= left < len(cur_map) and cur_map[left][0] <= timestamp:
            return cur_map[left][1]
        return ""
        
