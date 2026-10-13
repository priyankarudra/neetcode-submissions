class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        res = []
        
        for num in hash_set:
            if num-1 not in hash_set:
                res.append(num)

        max_count = 0
        count = 1
        for i in range(len(res)):
            next_num = res[i]
            for num in hash_set:
                next_num += 1
                if next_num not in hash_set:
                    break;
                if next_num in hash_set:
                    count+= 1
                
            max_count = max(max_count, count)
            count = 1

        return max_count


        