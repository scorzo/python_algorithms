#!/usr/bin/env python

# MERGE INTERVALS
#
# given a list of overlapping intervals, merge them to return a list of non-overlapping intervals
#
# NOTES
# - create new results[] list to return
# - sort sub lists by first values
# - copy first interval from intervals list to results list
# - iterate all remaining intervals
# - if start value of current interval is less than or equal to last item, end value in results list:
# - update the last item, end value in results list to be greater of end value current interval or last item, end value
# - otherwise, add current interval to results list


import argparse
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]] # add first pair to output

        for start, end in intervals:
            lastEnd = output[-1][1] # get the furthest value of output

            if start <= lastEnd: # if current item start less than furthest value of output
                # merge
                output[-1][1] = max(lastEnd, end) # extend last item of output by current item if current item is greater
            else:
                output.append([start, end]) # otherwise stick current item onto output
        return output


def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.merge([[1,3],[2,6],[8,10],[15,18]])  # [[1,6],[8,10],[15,18]]
    print(answer)

if __name__ == '__main__':
    main()


