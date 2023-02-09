#!/usr/bin/env python

# Anagram means using every single char in a word or phrase to create a new word or phrase.
# For example, "anagram" and "nagaram" are anagrams.
#   Method 1 is to create hashmaps for each of the 2 with a key for each char and a count of chars as the value. Next, compare the hashmaps.
#   Method 2 is to sort both strings and compare them. However, the space complexity of the sorting algorithm might make it less efficient.

import argparse
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.isAnagram("anagram", "nagaram")
    print(answer)

if __name__ == '__main__':
    main()


