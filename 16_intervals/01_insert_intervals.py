#!/usr/bin/env python

# INSERT INTERVALS
#
# - given an array of non-overlapping intervals in ascending order and an additional interval (which is possibly overlapping with the others), insert the new interval into the existing array, merging w/ existing intervals if necessary
#
# NOTES
#
# - create new results[] list to return
# - iterate list of intervals list
#
# - for each item in "insert into" list:
#     - if new range is (non-overlapping) before:
#     - insert new into results
#     - append the rest of the intervals
#     - return - we're done
# - else if new range is (non-overlapping) after:
#     - insert interval list item into results
# - else (must be overlapping)
# - overwrite new range by finding min from 2 lists and max from 2 lists
#
# - haven't found a place for new list yet, insert new range into list



import argparse
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.insert([[1,3],[6,9]], [2,5])  # [[1,5],[6,9]]
    print(answer)

if __name__ == '__main__':
    main()


