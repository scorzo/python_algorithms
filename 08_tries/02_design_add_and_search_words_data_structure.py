#!/usr/bin/env python

# DESIGN ADD AND SEARCH WORDS DATA STRUCTURE
#
# problem is similar to IMPLEMENT TRIE but must support dots (...) as wildcards in search method
# return true or false on search matc
# solution uses BACKTRACKING, RECURSION, DFS
# solution is exactly the same as IMPLEMENT TRIE except that it uses RECURSIVE DFS for the wildcard part
#
# NOTES
#
# pass root node to search method
# set cur variable to root node # use this to track position in TRIE
# call DFS method with index 0 and root node
# # note: index used for position of character in word we are looking for
# for loop over range of letters in word starting with index position
# if letter in children of node, set "cur" to that child and continue
# if letter not found in children of node, return false # we are done
# if wildcard '.' then:
#     increment current word index position by 1
#     run recursive DFS on every child character of this node
#     if any of the recursive calls returns true, then return true and continue w/ parent for loop


import argparse
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)

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


