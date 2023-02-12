#!/usr/bin/env python

# NETWORK DELAY TIME
#
# - given list of triplets indexed by node id: times[i] = {u,v,w}
# - u is source node, v is target node, w is weight
# - given node id k, calculate minimum time to reach all nodes
#
# NOTES
# - solution uses Dijkstra's algorithm (shortest path algorithm)
# - Dijkstra's algorithm uses BFS
# - main difference between Dikjstra's BFS and regular BFS is that WE ARE USING MINHEAP AS A PRIORITY QUEUE
#
# - create MINHEAP where LEFT SIDE IS TOTAL WEIGHT TO REACH NODE and right side is NODE ID
# - we are using BFS, so we traverse the graph by ADDING ALL NEIGHBORS OF CURRENT NODE TO PRIORITY QUEUE
# - at that point we just ADD THE NODE FROM THE PRIORITY QUEUE WITH THE SHORTEST WEIGHT TO OUR RESULTS LIST


import argparse
from typing import List

class Solution:

        def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
            # create adjacency map
            adj_map = {}

            # create priority queue
            pq = []

            # create visited set
            visited = set()

            # create results list
            results = []

            # populate adjacency map
            for time in times:
                if time[0] not in adj_map:
                    adj_map[time[0]] = []
                adj_map[time[0]].append([time[1], time[2]])

            # add starting node to priority queue
            pq.append([0, k])

            # while priority queue is not empty
            while pq:

                # pop off node with shortest distance
                node = heapq.heappop(pq)

                # if node is not visited
                if node[1] not in visited:

                    # add node to visited set
                    visited.add(node[1])

                    # add node to results list
                    results.append(node)

                    # add all neighbors to priority queue
                    if node[1] in adj_map:
                        for neighbor in adj_map[node[1]]:
                            heapq.heappush(pq, [neighbor[1] + node[0], neighbor[0]])

            # if number of nodes visited is not equal to number of nodes
            if len(visited) != n:
                return -1

            # return last node in results list
            return results[-1][0]


def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) # 2
    print(answer)

if __name__ == '__main__':
    main()


