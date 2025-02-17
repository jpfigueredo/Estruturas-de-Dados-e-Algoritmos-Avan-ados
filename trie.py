class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def display(self, node=None, level=0, prefix="Root"):
        """Displays the Trie structure in a tree format."""
        if node is None:
            node = self.root

        # Print the current node
        indent = "   " * level  # Indentation for hierarchy
        marker = " (word)" if node.is_end_of_word else ""  # Mark complete words
        print(f"{indent}|- {prefix}{marker}")

        # Recursively display children
        for char, child in sorted(node.children.items()):
            self.display(child, level + 1, char)

    def _dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)

        for char, child in node.children.items():
            self._dfs(child, prefix + char, results)

    def autocomplete(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        self._dfs(node, prefix, results)

        return results

if __name__ == "__main__":
    trie = Trie()
    words = ["and", "ant", "anthem", "android", "banana", "band", "bank", "bat", "batch"]
    for word in words:
        trie.insert(word)

    print(trie.autocomplete("an"))  # ['and', 'ant', 'anthem', 'android']
    print(trie.autocomplete("ban")) # ['banana', 'band', 'bank']
    print(trie.autocomplete("bat")) # ['bat', 'batch']
    print(trie.autocomplete("x"))   # [] (nenhuma palavra encontrada)
