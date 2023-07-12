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
        
    def find_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_words_from_node(node, prefix)
        
    def _get_words_from_node(self, node, prefix):
        results = []
        if node.is_word:
            results.append(prefix)
        for char in node.children:
            results.extend(self._get_words_from_node(node.children[char], prefix + char))
        return results
        
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")
print(trie.find_words_with_prefix("a")) # ['apple']
print(trie.find_words_with_prefix("b")) # ['banana']
print(trie.find_words_with_prefix("or")) # ['orange']
