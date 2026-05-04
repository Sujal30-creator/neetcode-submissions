class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start, end = max(nums), sum(nums)
        ans = max(nums)

        def isValid(capacity):
            arr_used = 1
            curr_sum = 0

            for w in nums:
                if curr_sum + w > capacity:
                    arr_used +=1
                    curr_sum = w
                else:
                    curr_sum += w

            return arr_used <= k

        while start<=end:
            middle = (start+end) // 2
            if isValid(middle):
                ans = middle
                end = middle-1
            else:
                start = middle+1
        return ans