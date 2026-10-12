class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # linear scan
        # store the complement in hashmap

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            else:
                hashmap[target - nums[i]] = i

            
            

            
            
        