class TimeMap:

    def __init__(self):
        self.db = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.db[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.db[key]
        if len(arr) == 0:
            return ""
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left +right) // 2
            if arr[mid][0] > timestamp:
                right = mid - 1
            elif arr[mid][0] < timestamp:
                left = mid + 1
            else:
                return arr[mid][1]
        if arr[right][0] <= timestamp:
            return arr[right][1]
        return ""

