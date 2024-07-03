from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = {} 

        for i, num in enumerate(nums): 
            diff = target - num 

            if diff in num_list: 
                return [i, num_list[diff]]
            else: 
                num_list[num] = i

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Indices: {result}")  # Output: Indices: [1, 0]