class TimeMap:
    def __init__(self):
        self.hashmap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append([timestamp,value])
        else:
            self.hashmap[key] = [[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            nums = self.hashmap[key]
            start, end = 0, len(nums)-1
            ans = ""
            
            while start<=end:
                middle = (start+end)//2
                if nums[middle][0] == timestamp:
                    return nums[middle][1]
                elif nums[middle][0] < timestamp:
                    ans = nums[middle][1]
                    start = middle+1
                else:
                    end = middle-1
            return ans
        else:
            return ""
        
