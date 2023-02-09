#!/usr/bin/env python

import argparse
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # Your code here
    solution = Solution()
    answer = solution.containsDuplicate([1,2,3])
    print(answer)

if __name__ == '__main__':
    main()


