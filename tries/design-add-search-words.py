class TrieNode: 
    def __init__(self):
        self.endOfWord = False 
        self.children = {} 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        cur = self.root 
        for c in word: 
            if c not in cur.children: 
                cur.children[c] = TrieNode()
            cur = cur.children[c] 
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        # define a helper function so that we can recursively call it
        def search_helper_dfs(node, index):
            # instead of a for loop going through each character, we are
            # using an index because if we reach "." then we want to skip 
            # it and start at the (index+1)th index to the end of the len
            # of the word
            for i in range(index, len(word)):
                if word[i] == ".":
                    # for each child at the current node we're at
                    # we will call the search_helper_dfs function
                    # to traverse each child path to see if there's
                    # a word
                    for child in node.children.values():
                        # i + 1 (skipping the ".")
                        # if search_helper_dfs returns
                        # true then that means we reached the 
                        # endOfWord
                        if search_helper_dfs(child, i + 1):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            return node.endOfWord

        return search_helper_dfs(self.root, 0)

# Example usage
obj = WordDictionary()
obj.addWord("apple")
print(obj.search("app.e"))  # Should return True
print(obj.search("app"))  # Should return False