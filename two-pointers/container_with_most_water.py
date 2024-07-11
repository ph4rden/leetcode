from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_amount = 0

        while l < r: 
            # area = length x width 
            length = min(height[l], height[r])
            width = r - l 
            area = length * width 

            max_amount = max(max_amount, area)

            if height[l] < height[r]: 
                l += 1
            elif height[l] > height[r]: 
                r -= 1
            else: 
                r -= 1
        return max_amount
