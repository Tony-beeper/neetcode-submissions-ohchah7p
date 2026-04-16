import bisect
class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((value, timestamp))
    def get(self, key: str, timestamp: int) -> str:
        if not self.dict.get(key):
            return ""
        
        lst = self.dict.get(key)
        times = [time for _, time in lst]

        idx = bisect.bisect_right(times, timestamp)
        if times[idx-1] <= timestamp:
            return lst[idx-1][0]
        return ""
        
