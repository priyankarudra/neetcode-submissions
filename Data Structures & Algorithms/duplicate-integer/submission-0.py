from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = Counter(nums)

        if len(res) == len(nums):
            return False
        
        return True


        