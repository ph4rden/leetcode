from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # global list
        # sol array is a temp that is going to change a lot by appending/popping 
        res, sol = [], []

        def backtrack(i): 
            # start with base case sol and that is if it goes out of bounds
            if i == len(nums): 
                # give result variable a copy of sol
                res.append(sol[:])
                return
            
            # left path aka dont pick the number at index i
            backtrack(i+1)

            # right path
            sol.append(nums[i]) # temporarily pick it
            backtrack(i+1)
            sol.pop() # pop that exact same number to undo
        
        backtrack(0)
        return res

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets(nums))  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]