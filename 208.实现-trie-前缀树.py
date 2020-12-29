#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self, val=None, end=True):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.end = end
        self.val = val

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return
        if word[0] not in self.children:
            self.children[word[0]] = Trie(word[0], len(word) == 1)
        c = self.children[word[0]]
        if len(word) == 1:
            c.end = True
        c.insert(word[1:])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return True
        if word[0] not in self.children:
            return False
        else:
            c = self.children[word[0]]
            if len(word) == 1:
                return c.end
            else:
                return c.search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True
        if prefix[0] not in self.children:
            return False
        else:
            c = self.children[prefix[0]]
            return c.startsWith(prefix[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
