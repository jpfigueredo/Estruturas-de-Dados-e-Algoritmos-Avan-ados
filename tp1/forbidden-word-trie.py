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

    def contains_prohibited_word(self, text):
        words = text.lower().split()
        for word in words:
            if self.search(word):
                return True, word
        return False, None

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

trie = Trie()
prohibited_words = ["palavrão", "ofensivo", "insulto"]
for word in prohibited_words:
    trie.insert(word)
text = "Este comentário contém um insulto"
found, word = trie.contains_prohibited_word(text)
if found:
    print(f"🚫 Palavra proibida detectada: '{word}'")
else:
    print("✅ Nenhuma palavra proibida encontrada.")

