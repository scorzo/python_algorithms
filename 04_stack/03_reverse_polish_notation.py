#!/usr/bin/env python

# EVALUATE REVERSE POLISH NOTATION
#
# - RPN is an alternative to infix notation which is the standard way of writing expressions in algebra with operator precedence, etc.
# - with RPN, the operator comes after the number and parenthetic precedence is replaced by putting operators in the correct order in the series of characters
#
# - example:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#
# - task is to receive a string of chars (numbers and operators) in RPN and calculate the result
#
# NOTES
#
# - O(n) time complexity
# - O(n) memory complexity
# - uses stack
# - for each input string character
# - add number to stack
# - when you reach an operator:
# - apply the operator to the last 2 values on the stack
# - pop the last 2 operators from the stack
# - add the calculated value to the stack
# - continue through the input string


import argparse
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(answer)

if __name__ == '__main__':
    main()


