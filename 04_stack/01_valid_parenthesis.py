#!/usr/bin/env python

# VALID PARENTHESIS
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# NOTES
# - uses a stack, which is just a list in this case
# - stack is used to hold the brackets we've seen and haven't found a match for yet - once we find a match, we remove the match from the stack


import argparse
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map: # must be opening
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]: # must be closing - using map, should pair up with last stack item
                return False
            stack.pop()

        return not stack

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.isValid("()[]{}")
    print(answer)

if __name__ == '__main__':
    main()


