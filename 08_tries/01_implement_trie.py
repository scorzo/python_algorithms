#!/usr/bin/env python

# IMPLEMENT TRIE
# - write a trie class that:
#     - accepts new words
#     - searches on prefix strings and returns true if found
#     - searches on whole words and returns true if found
#
# NOTES
#
# - note that if we were just searching for whole words, we could use a HASHMAP or a HASHSET, but since we are doing prefix searches, we are doing the CHARACTER BASED TREE STRUCTURE:
#
#     - each node is a character
#     - technically EACH NODE IS A CLASS THAN CONTAINS A HASHMAP that contains the letters on that "layer" of the tree - that value for each letter key is an instance of the node class
#     - if it's the last character in a word, we note that on the node (but the node can still have children characters)


import argparse
from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.maxProfit([7,1,5,3,6,4])
    print(answer)

if __name__ == '__main__':
    main()


