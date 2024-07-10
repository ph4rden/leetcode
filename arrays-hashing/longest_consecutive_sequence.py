# my first sol: 
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort() # sort the array
        count = 1
        largest = 1

        if len(nums) == 0: 
            return 0

        for i in range(len(nums) - 1): 
            if nums[i] == nums[i+1]: # if the next number is the same, ignore
                continue
            elif nums[i] + 1 == nums[i+1]: 
                count += 1 
            else: 
                largest = max(count, largest) 
                count = 1
        
        return max(largest,count)