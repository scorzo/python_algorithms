#!/usr/bin/env python

# - task is to look for duplicates
#     - one way is brute force:
#     - compare every value to every value
#     - time complexity is O (n^2) where n is size of array
#     - memory complexity is nothing: O (1)
# - you could sort array and go through one by one comparing adjacent values
# - time complexity for going through array is O (n)
# - time complexity for sorting is O (n log n)
# - memory complexity not including sorting alogrithm O (1)
# - memory complexity including sorting algorithm ?
# - better way is to use a hashset (using set()) - it uses more memory though
# - time complexity to populate hashset is O (n)
# - memory complexity is O (n)

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
    def containsDuplicate2(self, nums: List[int]) -> bool:
        hashset = set(nums)
        return len(nums) != len(hashset)

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.containsDuplicate([1,2,3])
    print(answer)

if __name__ == '__main__':
    main()


