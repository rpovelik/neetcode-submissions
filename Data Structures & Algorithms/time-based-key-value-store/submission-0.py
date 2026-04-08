import bisect

class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        else:
            closest = bisect.bisect_right(self.map[key], timestamp, key=lambda x: x[0]) - 1

            if closest == -1:
                return ""

            t, v = self.map[key][closest]
            return v