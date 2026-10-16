class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        left = 0
        right = length-1
        max_area = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            max_area = max(max_area, area)

            if height == heights[left]:
                left += 1
            else:
                right -= 1
        
        return max_area
        


        