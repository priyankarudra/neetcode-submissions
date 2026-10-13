from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)

        sorted_nums_count = dict(sorted(nums_count.items(), key=lambda item: item[1]))

        return list(sorted_nums_count)[-k:]

        



        