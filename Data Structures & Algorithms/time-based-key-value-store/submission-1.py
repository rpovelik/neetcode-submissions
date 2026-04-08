import bisect

class TimeMap:

    def __init__(self):
        self.m = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        
        self.m[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""

        idx = bisect.bisect_right(self.m[key], timestamp, key=lambda x: x[0])

        return self.m[key][idx - 1][1] if idx > 0 else ""

