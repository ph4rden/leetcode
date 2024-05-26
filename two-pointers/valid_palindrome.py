'''
    1. clean the string of anything that isnt a letter or a number
    2. convert to all lowercase 
    3. use 2 ptr approach to compare the first character/last character, then so on and so forth
    4. return boolean 
'''

# first solution, will revisit for more optimal later
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for char in s: 
            if char.isalnum(): 
                cleaned.append(char.lower())
        cleaned_str = ''.join(cleaned)
        
        ptr1, ptr2 = 0, len(cleaned_str) - 1
        while ptr1 < ptr2: 
            if cleaned_str[ptr1] != cleaned_str[ptr2]:
                return False 
            ptr1 += 1
            ptr2 -= 1
        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))