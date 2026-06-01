class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, k
        hashmap = dict()

        for i in range(len(nums)):
            if i <= right:
                if nums[i] in hashmap:
                    return True
                else:
                    hashmap[nums[i]] = 1
                if i == right:
                    del hashmap[nums[left]]
                    right+=1
                    left+=1

        return False