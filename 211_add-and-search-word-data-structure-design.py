# https://leetcode.com/problems/add-and-search-word-data-structure-design/
import collections
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(set)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.d[len(word)].add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        n = len(word)
        for dict_word in self.d[n]:
            i = 0
            while i < n and (dict_word[i] == word[i] or word[i] == '.'):
                i += 1
            if i == n:
                return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)