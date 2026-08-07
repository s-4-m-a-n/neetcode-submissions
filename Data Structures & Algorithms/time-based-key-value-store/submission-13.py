class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].append((value, timestamp))
        else:
            self.hash_map[key] = [(value, timestamp)]

    # def get(self, key: str, timestamp: int) -> str:
    #     values = self.hash_map.get(key, [])
    #     if len(values) == 0:
    #         return ""
            
    #     l, r = 0, len(values)-1
    #     res = ""

    #     while l<=r:
    #         p = l+r//2
    #         m_t = values[p][1]
    #         if m_t > timestamp:
    #             r = p-1
    #         else:
    #             res = values[p][0]
    #             l = p+1
    #     return res
    def get(self, key: str, timestamp: int) -> str:
        values = self.hash_map.get(key, [])
        if len(values) == 0:
            return ""
  
        l, r = 0, len(values)-1
        res_v = ""

        while l <= r:            
            m = (l + r)//2
            m_t = values[m][1]
            
            if m_t > timestamp:
                r = m - 1
            else:
                res_v = values[m][0]
                l = m + 1

        return res_v
