#!/usr/bin/env python

# - given char string and target int, find the longest string of any repeating single character
# - note that you can replace target int number of chars with any letter of the alphabet
#
# NOTES
#
# - uses sliding window technique
# - uses two pointers
# - uses hashmap
# - note that the hashmap is counting all instances only within the working range
# - for each range of chars within pointers
#     - find most common char
#     - subtract number instances common char from target
#         - if greater than target, move left sliding window pointer to the right and start a new iteration
#         - if less than target:
#             - add entry to hashmap as letter:count
#     - move the right pointer to the right


import argparse
from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.characterReplacement("ABAB", 2)
    print(answer)

if __name__ == '__main__':
    main()


