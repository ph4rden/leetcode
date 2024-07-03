from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = {} 

        for num in nums: 
            if num in dups: 
                return True
            dups[num] = True
        return False

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    result = solution.containsDuplicate(nums)
    print(f"Does the list {nums} contain duplicates? {result}")  # Output: True
    
    nums = [1, 2, 3, 4]
    result = solution.containsDuplicate(nums)
    print(f"Does the list {nums} contain duplicates? {result}")  # Output: False