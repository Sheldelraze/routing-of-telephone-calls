import unittest

from libs.trie import Trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()
        self.trie.insert("1", 0.9)
        self.trie.insert("268", 5.1)
        self.trie.insert("46", 0.17)
        self.trie.insert("467", 0.9)
        self.trie.insert("4673", 1.1)

    def test_insert_and_search(self):
        self.assertEqual(self.trie.search("1"), 0.9)
        self.assertEqual(self.trie.search("268"), 5.1)
        self.assertEqual(self.trie.search("46"), 0.17)
        self.assertEqual(self.trie.search("467"), 0.9)
        self.assertEqual(self.trie.search("4673132312"), 1.1)

    def test_search_no_match(self):
        self.assertIsNone(self.trie.search("999"))
