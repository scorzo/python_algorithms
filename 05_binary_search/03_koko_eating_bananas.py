#!/usr/bin/env python

# KOKO EATING BANANAS
#
# - given list of quantities of bananas and a target number of hours "h"
# - return the minimum banana eating speed-per-hour k where
# - all bananas eaten in "h" hours
# - can only eat from one pile per hour
#
# NOTES
#
# - think of it as a series of successive rooms each separated by a door - the next door only opens when the bananas in the current room are finished - you can spend as many hours in each room as you'd like, but you need to finish going through the rooms in "h" hours - what is the smallest hourly banana group size you could eat to make this possible?
#
# - based on the above premise, the max you could eat in an hour would be the amount in the room with the most in it
#
# - also, if there were more piles (rooms) than hours, then it wouldn't be possible
#
# - so you don't want hours left over, and you don't want to get stuck in a room with unfinished bananas at the end of h hours
#
# - brute force by trying every value from 1 to max number of bananas in a pile
# - but apply binary search to the brute force to reduce time complexity to O (log(max P) * P) vs O ((max P) * P)
# - for example:
#     - select the middle value
#     - divide each number by the middle value and round up
#     - tally up the count of hours
#     - if it is under the hours, we can eat slower, so move test range to left
#     - if it exceeds the hours, we can eat faster, so move the range to the right



import argparse
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # range - number of bananas we are trying as solution
        k = 0

        while l <= r:
            m = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += ((p - 1) // m) + 1
            if totalTime <= h: # we have hours left over
                k = m # this is our best guess so far - save it
                r = m - 1 # try eating fewer
            else: # we didn't eat enough bananas
                l = m + 1 # try eating more
        return k

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.minEatingSpeed([3,6,7,11], 8) # 4
    print(answer)

if __name__ == '__main__':
    main()


