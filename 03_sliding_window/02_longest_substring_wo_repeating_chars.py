#!/usr/bin/env python

# - given a character string, find longest substring without repeating chars
#
# NOTES
#
# - uses sliding window technique
# - two pointers
# - use a set ( set() ) to record which chars have been seen and to check for duplicates
#     - if duplicate:
#           keep removing the leftmost char from the charset until the duplicate char is no longer in the character set
#           - next add the character at pointer r to the charset,
#           measure the distance from l to r pointer and keep if longer than any others you've seen so far

import argparse
from typing import List



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.lengthOfLongestSubstring("abcabcbb")
    print(answer)

if __name__ == '__main__':
    main()


