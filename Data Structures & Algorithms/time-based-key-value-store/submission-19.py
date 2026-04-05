import bisect
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        cur_map = self.timemap[key]
        time = [t for t, _ in cur_map]
        left = bisect.bisect_right(time, timestamp) - 1
        if 0 <= left < len(cur_map):
            return cur_map[left][1]
        return ""
        
