from typing import List
'''
    1. sort words
    2. check if sorted word is in the dict
    3. use sorted word as the key with the value being the word
    4. return a list of the values from the dict
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
                
            anagrams[sorted_word].append(word)
        
        # Return the list of grouped anagrams
        return list(anagrams.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))