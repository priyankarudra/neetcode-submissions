class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_max = [0] * length
        right_max = [0] * length
        total_water = 0
  
        left_height_max = 0
        for i in range(length):
            left_height_max = max(left_height_max, height[i])
            left_max[i] = left_height_max

        right_height_max = 0
        for j in range(length-1, -1, -1):
            right_height_max = max(right_height_max, height[j])
            right_max[j] = right_height_max

        for k in range(length):
            trapped_water = min(left_max[k], right_max[k]) - height[k]
            total_water += trapped_water
        
        return total_water
        

            

        