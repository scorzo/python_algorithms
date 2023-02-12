#!/usr/bin/env python

# MIN STACK
#
# - write a class that supports stack operations, push, pop (remove off top) and top (get top value) - plus write a method for retrieving min value on stack
# - note: need to write the min value method with 0(1) complexity time
#
# NOTES
#
# - note that our class supports maintaining 2 parallel stacks that are in sync: main value and min value
#
# - the way to write the min value method w/ 0(1) is to have a parallel stack recording the min value so far at every point - each time you pop a value off the top, you still know the min value at the new highest index



import argparse
from typing import List

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.minStack([2,7,11,15], 9)
    print(answer)

if __name__ == '__main__':
    main()


