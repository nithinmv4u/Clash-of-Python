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
        
    def longest_prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                break
            prefix += char
            node = node.children[char]
            if node.is_word:
                return prefix
        return ""
        
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")
print(trie.longest_prefix("apples")) # 'apple'
print(trie.longest_prefix("bandana")) # 'ban'
print(trie.longest_prefix("pear")) # ''
