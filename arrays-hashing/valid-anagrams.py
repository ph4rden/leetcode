class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        valid = {}

        if len(s) != len(t): 
            return False 
        
        for letter in s: 
            if letter not in valid: 
                valid[letter] = 1
            else: 
                valid[letter] += 1
        
        for letter in t: 
            if letter not in valid or valid[letter] == 0: 
                return False
            else: 
                valid[letter] -= 1
        
        return all(count == 0 for count in valid.values())

# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s, t)
    print(f"Is '{s}' an anagram of '{t}'? {result}")  # Output: True
    
    s = "rat"
    t = "car"
    result = solution.isAnagram(s, t)
    print(f"Is '{s}' an anagram of '{t}'? {result}")  # Output: False