#!/usr/bin/env python

# MIN COST TO CONNECT ALL POINTS
#
# WHAT IS A MINIMUM SPANNING TREE (MST)?
# A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
#
# In other words, given a set of nodes with various connections (edges), an MST is a subset of those edges which connect the vertices together (without any cycles and with the minimum possible total edge weight).
#
# In the problem below, we are not given edges, so we are assuming that all possible edges exist to begin with.  See this photo for visual reference: https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Minimum_spanning_tree.svg/600px-Minimum_spanning_tree.svg.png
#
# NOTES
# - this is a MINIMUM SPANNING TREES (MST) problem
# - uses PRIM'S MIN PATH ALGORITHM (which is similar to DJIKSTRA'S MIN PATH ALGORITHM)
# - calculate cost of each edge using manhattan distance which means traveling from point to point along right angles rather than diagonally
#
#                                                                                                                                 - observations on PRIM'S ALGORITHM:
#                                                                                                                                                       - number of edges will be number of nodes minus 1 (n -1)
#                                                                                                                                                                                                       - solution will not have any cycling edges (no loops)
# - solution will give us the minimum possible distance
#
#                                              - step 1 is to calculate edges using manhattan distance
#                                                                                             - step 2 is to apply PRIM'S ALGORITHM to get optimal solution
#
#                                                                                                                      - time complexity O(n^2 log n) # where n is number of points given - log n comes from PRIM'S ALGORITHM since we are using MIN HEAP
#
# - going to use BFS
#                - going to use 3 data structures:
#
# 1) HASH REF (ADJACENCY MAP) # nodes and distances - indexed by both directions
# 2) MIN HEAP (FRONTIER)
# 3) SET (visited)
#
#
#    - pick a starting node
#                      - create a "visited" data structure (SET) so that we avoid creating CYCLES
#                                                                                          - create a MIN HEAP for tracking FRONTIER of our BFS
# - FRONTIER will contain value pairs for every node respective to a single node, {EDGE_WEIGHT, NODE_ID}  where EDGE_WEIGHT is the distance between the 2 nodes
# - we do this check for each of the nodes (measure distance to all other nodes) and add those to the same MIN HEAP (FRONTIER)
# - our BFS will involve popping values off of our MIN HEAP (FRONTIER) and then adding the node ID to our VISIT (SET)
# - how do we know when to we have arrived at our solution and we can stop BACKTRACKING? when our solution is number of nodes - 1 (n-1)


import argparse
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create adjacency map
        adj_map = {}

        # create priority queue
        pq = []

        # create visited set
        visited = set()

        # create results list
        results = []

        # populate adjacency map
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    if i not in adj_map:
                        adj_map[i] = []
                    adj_map[i].append([j, self.manhattan_distance(points[i], points[j])])

        # add starting node to priority queue
        pq.append([0, 0])

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

                # add neighbors to priority queue
                for neighbor in adj_map[node[1]]:
                    heapq.heappush(pq, [neighbor[1], neighbor[0]])

        # return sum of results
        return sum([result[0] for result in results])

    def manhattan_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.manhattan_distance([0,0], [2,2])  # 4
    answer2 = solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])  # 20
    print(answer)

if __name__ == '__main__':
    main()


