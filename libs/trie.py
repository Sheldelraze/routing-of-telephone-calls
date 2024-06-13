class TrieNode:
    def __init__(self):
        self.children = {}
        self.rate = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, prefix: str, rate: float):
        node = self.root
        for char in prefix:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.rate = rate

    def search(self, phone_number: str) -> float:
        node = self.root
        max_rate = None

        for char in phone_number:
            if char in node.children:
                node = node.children[char]
                if node.rate is not None:
                    max_rate = node.rate
            else:
                break

        return max_rate
