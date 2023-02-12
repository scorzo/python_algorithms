#!/usr/bin/env python

# WORDSEARCH II (BACKTRACKING TRIE)
#
# - given m x n matrix of letters
# - given list of words
# - return which of list of words is in matrix of letters
# - letters can be connected vertically and horizontally - no reusing letters in a word
#
# NOTES
#
# - populate a trie with the list of words
#
# - create "results" set() for list of found words
# - create "visit" set() for board nodes
#     - DFS method: # receives: board coords, root trie node, "found" word string (starts with "")
# - check if children of TRIE node contains board node letter
# - if not, return FALSE
# - add board coords to visit set()
# - move trie node pointer to matching child (for upcoming DFS call)
# - append board letter to word string (i.e., "be")
# - if TRIE node is wordEnd, add word to results set()
# - call DFS on board coords (top, bottom, left, right) passing in TRIE node and word string ("be")
# - remove board coords from visit set()
#
# - iterate board coordinates starting top left:
# - call DFS on each one:


import argparse
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                    r < 0
                    or c < 0
                    or r == ROWS
                    or c == COLS
                    or board[r][c] not in node.children
                    or node.children[board[r][c]].refs < 1
                    or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

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


