#!/usr/bin/env python

# NON-OVERLAPPING INTERVALS
#
# - given an array of overlapping interval pairs
# - return the minimal number of interval pairs you'd need to remove to make the intervals non-overlapping
#
# NOTES
# - sort
# - move through pairs
# - if pairs overlap, remove the one that extends further


import argparse
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.maxProfit([7,1,5,3,6,4])
    print(answer)

if __name__ == '__main__':
    main()


