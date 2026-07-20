class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        j=0

        for _ in range(hashmap.get(0,0)):
            nums[j] = 0
            j+=1

        for _ in range(hashmap.get(1,0)):
            nums[j] = 1
            j+=1


        for _ in range(hashmap.get(2,0)):
            nums[j] = 2
            j+=1