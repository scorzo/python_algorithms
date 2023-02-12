#!/usr/bin/env python

# LAST STONE WEIGHT
#
# - this is a game where you start with a list of stone weights
# - pop off the top 2 heaviest stones
# - if they are equal, they both disappear
# - if one is bigger than the other, subtract the difference and make a new stone with that weight
# - keep going until you have either one stone or no stones - return the weight of the last stone or 0
#
# NOTES
# - similar solution to Kth LARGEST in that it uses a HEAP
# - in this case it uses a MAX HEAP which is not implemented in python - in order to achieve this we use a HEAP making all integers negative which does the same thing
#
# SOLUTION
# - heapify the list
# - reduce function:
# - pop top 2 heaviest
# - compare and either remove both or add new stone to heap with new weight
#
# while list <= 2:
#     run reduce function


import argparse
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, y-x)
        return -stones[0] if stones else 0

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.lastStoneWeight([2,7,4,1,8,1])    # 1
    print(answer)

if __name__ == '__main__':
    main()


