class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]
        return True

if __name__ == "__main__":
    # Example usage
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # returns True
    print(trie.search("app"))     # returns False
    print(trie.startsWith("app")) # returns True
    trie.insert("app")
    print(trie.search("app"))     # returns True