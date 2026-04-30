class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums)-1

        while (start<=end):
            middle = (start+end)//2
            if (nums[start] == target or nums[middle] == target or nums[end] == target):
                return True
            
            if (nums[start] <= nums[middle]):
                if (nums[start]==nums[end]):
                    start+=1
                    end-=1
                elif nums[start]<= target and nums[middle]>target:
                    end = middle-1
                else:
                    start = middle+1
            else:
                if nums[middle]<target and nums[end]>= target:
                    start=middle+1
                else:
                    end=middle-1

        return False