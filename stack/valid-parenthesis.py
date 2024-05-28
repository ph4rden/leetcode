'''
    create a dict to map opening and closing brackets?
    1. traverse string, push opening brackets, pop closing brackets?
    2. check to see if stack is empty (true if empty false if not)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
    
        for char in s: 
            if char == '{' or char == '(' or char == '[': 
                stack.append(char)
            else: # make sure to check if stack is empty, can cause issues
                if stack and brackets[char] == stack[-1]:
                    stack.pop()
                else: 
                    return False
        return len(stack) == 0
                
sol = Solution()
print(sol.isValid('(]'))