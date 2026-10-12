class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create an array for prefix product
        # create an array for suffix product

        length = len(nums)
        prefix_prod = [0] * length
        suffix_prod = [0] * length
        res = [0] * length

        prefix_prod[0] = 1
        suffix_prod[length - 1] = 1

        for i in range(1, length):
            prefix_prod[i] = nums[i-1] * prefix_prod[i-1]

        for j in range(length-2, -1, -1):
            suffix_prod[j] = nums[j+1] * suffix_prod[j+1]
        
        for k in range(length):
            res[k] = prefix_prod[k] * suffix_prod[k]

        return res

        
        