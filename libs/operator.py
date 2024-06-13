from libs.trie import Trie


class Operator:
    def __init__(self, name: str):
        self.name = name
        self.prefix_trie = Trie()

    def insert_prefix(self, prefix: str, rate: float):
        self.prefix_trie.insert(prefix, rate)

    def get_rate(self, phone_number: str) -> float:
        return self.prefix_trie.search(phone_number)
