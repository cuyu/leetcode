#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
class TreeNode:
    def __init__(self, val: str) -> None:
        self.val = val
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode('')

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode(c)
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return False

        def _search(node: TreeNode, w: str) -> bool:
            for i, c in enumerate(w):
                if c != '.':
                    if c not in node.children:
                        return False
                    else:
                        node = node.children[c]
                else:
                    for n in node.children.values():
                        if _search(n, w[i+1:]):
                            return True
                    else:
                        return False
            return node.end
        return _search(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
if __name__ == "__main__":
    d = WordDictionary()
    d.addWord('a')
    d.addWord('a')
    d.search('.a')
