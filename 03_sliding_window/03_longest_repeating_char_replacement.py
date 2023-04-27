#!/usr/bin/env python

# You are given a string s and an integer k.
# You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after
# performing the above operations.
#
# NOTES
#
# - uses sliding window technique
# - uses two pointers
# - uses hashmap
# - note that the hashmap IS COUNTING ALL INSTANCES ONLY WITHIN WINDOW
# - for each range of chars within pointers
#     - find most common char
#     - subtract number instances common char from target
#         - if greater than target, move left sliding window pointer to the right and start a new iteration
#         - if less than target:
#             - add entry to hashmap as letter:count
#     - move the right pointer to the right


import argparse
from typing import List


# search string looking for max subsequent recurring chars with k replacements


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # most frequent character in current window
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
    answer = solution.characterReplacement("ABAB", 2)   # 4
    print(answer)

if __name__ == '__main__':
    main()


