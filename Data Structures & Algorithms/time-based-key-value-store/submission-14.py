class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].append((value, timestamp))
        else:
            self.hash_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        values = self.hash_map.get(key, [])
        if len(values) == 0:
            return ""
        l, r = 0, len(values)-1
        res = ""
        while l<=r:
            p = (l+r)//2
            if values[p][1] > timestamp:
                r = p-1
            else:
                res = values[p][0]
                l = p+1
        return res
