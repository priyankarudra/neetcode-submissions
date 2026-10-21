class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for ele in s:
            if ele in hash_map:
                if not stack or stack[-1] != hash_map[ele]:
                    return False
                stack.pop()
            else:
                stack.append(ele)
        
        return len(stack) == 0

                


        