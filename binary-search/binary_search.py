'''
    1. Left ptr, Middle ptr, Right ptr
    2. Find median, check if median is < or > target
    3. If less than, set Right ptr to middle, recalculate median value and vice versa for greater than
    4. Repeat until target index is found, otherwise return -1

    mistakes made 5/29: 
        - while condition
        - incr/decr middle by 1
        - floor division (// instead of /)
'''
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = r//2

        while l <= r: 
            if nums[m] == target: 
                return m
            elif nums[m] < target: 
                l = m + 1
                m = (l+r)//2
            elif nums[m] > target: 
                r = m - 1
                m = (l+r)//2
        return -1

sol = Solution()
print(sol.search([1,2,3], 3))
