from typing import List

# first sol 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1

        # adjust lp if desired val is greater than value at lp

        while lp < rp: 
            total = numbers[lp] + numbers[rp]
            if total == target: 
                return [lp+1, rp+1]
            elif total < target: 
                lp += 1
            elif total > target: 
                rp -= 1
        return []
        