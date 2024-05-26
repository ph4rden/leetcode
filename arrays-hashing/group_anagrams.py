from typing import List


'''
    
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            # Sort the word to form the key
            sorted_word = ''.join(sorted(word))
            
            # If the key is not in the dictionary, create a new list
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
                
            # Append the original word to the list corresponding to the sorted word
            anagrams[sorted_word].append(word)
        
        # Return the list of grouped anagrams
        return list(anagrams.values())

# Example usage:
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))