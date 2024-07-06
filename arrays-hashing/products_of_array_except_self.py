from typing import List

#brute force
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = []

#         for i in range(len(nums)): 
#             temp = 1 
#             for j in range(len(nums)): 
#                 if i != j: 
#                     temp *= nums[j]
#             res.append(temp)
#         return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1 
        res = [0] * (len(nums))

        for i in range(len(nums)): 
            res[i] = prefix 
            prefix *= nums[i]
        for j in range(len(nums)-1, -1, -1): 
            res[j] *= postfix 
            postfix *= nums[j]
        return res

if __name__ == "__main__":
    nums = [1,2,3,4] 
    sol = Solution()
    print(sol.productExceptSelf(nums))
    