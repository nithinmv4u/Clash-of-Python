class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
        
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")
print(trie.search("apple")) # True
print(trie.search("banana")) # True
print(trie.search("pear")) # False
