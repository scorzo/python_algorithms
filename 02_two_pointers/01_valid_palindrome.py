#!/usr/bin/env python

# - palindrome reads same backwards and forwards
# - check if it's a palindrome, skipping non-alphanumeric chars
#
# - write func that uses ascii codes to see if alphanumeric - use python ord()
# - left pointer, right pointer - in while (left < right) loop, increment left, decrement right compare left and right chars

import argparse
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
                ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
        )

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.isPalindrome("taco cat")
    print(answer)

if __name__ == '__main__':
    main()


