class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L, R = 0, k
        ans = list()

        while R<=len(nums):
            ans.append(max(nums[L:R]))
            L+=1
            R+=1

        return ans