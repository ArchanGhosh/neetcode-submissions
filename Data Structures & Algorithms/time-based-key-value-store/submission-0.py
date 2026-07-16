from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_dict or not self.time_dict[key]:
            return ""
        
        _curr = self.time_dict[key]

        l, r = 0, len(_curr)-1

        closest = -1

        while l<=r:
            mid = (l+r)//2

            if _curr[mid][-1]<=timestamp:
                l = mid+1
                closest = mid
            else:
                r = mid-1
            


        return _curr[closest][0] if closest != -1 else ""
            

        
