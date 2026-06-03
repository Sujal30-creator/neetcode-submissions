class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        max_length = len(nums)
        flag = False
        sum = 0
        
        for right in range(len(nums)):
            while sum + nums[right] >= target:
                max_length = min(max_length, right - left + 1)
                sum -= nums[left]
                left += 1
                flag = True

            sum += nums[right]
        
        return max_length if flag == True else 0