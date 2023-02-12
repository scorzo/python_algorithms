#!/usr/bin/env python

# K CLOSEST POINTS TO ORIGIN
#
# - given list of coordinate points and an integer "k", return k number of points that are closest to origin (0,0) using EUCLIDEAN DISTANCE
#
# - EUCLIDEAN DISTANCE IS:
#
# SQUARE_ROOT_OF ( (x2 - x1)^2 + (y2 - y1)^2 )
#
# SOLUTION
#
# - no need to calculate square root - comparing the sum of the square values is enough
# - use heapify minheap which has operational time complexity of O (n)
# - pop k number of items from list for the closest ones
# - note, the calculated distance should be the first item in each list item so that heapify can sort based on that value
# - time complexity for popping is k * log n


import argparse
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(minHeap, (distance, point))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(minHeap)[1])
        return result

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.kClosest([[1,3],[-2,2]], 1)    # [[-2,2]]
    print(answer)

if __name__ == '__main__':
    main()


