class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = "".join([char for char in s if char.isalnum()])
        lowercase_text = alpha_num.lower()
        
        left = 0
        right = len(lowercase_text) - 1

        while left < right:
            if lowercase_text[left] != lowercase_text[right]:
                return False

            left += 1
            right -= 1

        return True
        
        