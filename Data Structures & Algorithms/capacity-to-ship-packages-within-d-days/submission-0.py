class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = max(weights), sum(weights)
        ans = max(weights)

        def isValid(capacity):
            days_used = 1
            current_sum = 0

            for w in weights:
                if current_sum + w > capacity:
                    days_used += 1
                    current_sum = w
                else:
                    current_sum += w

            return days_used <= days

        while start<=end:
            middle = (start+end) // 2
            if isValid(middle):
                ans = middle
                end = middle-1
            else:
                start = middle+1
        return ans