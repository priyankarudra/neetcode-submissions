from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            ele = "".join(sorted(strs[i]))

            if ele in hashmap:
                hashmap[ele].append(strs[i])           

            if ele not in hashmap:
                hashmap[ele].append(strs[i])
            
        res = list(hashmap.values())

        return res
        