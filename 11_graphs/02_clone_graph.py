#!/usr/bin/env python

# CLONE GRAPH
# - given a reference node in a connected undirected graph,
# - return a deep copy (clone) of the graph
# - each node in the graph contains a value (int) and a list (of its neighbors)
#
# NOTES
# - uses an ADJACENCY LIST
# - for ADJACENCY LIST, use HashMap (like almost all graph related problems) to map old nodes to their new node counterparts
# - this one uses DFS (but you could use BFS search as well)
# - time operation is O (n) = E + V # where E is edges and V is vertices (in this case nodes)


import argparse
from typing import List

class Solution:
    def cloneGraph(self, node):
        # create hashmap
        visited = {}

        # call helper function
        return self.dfs(node, visited)

    def dfs(self, node, visited):
        # if node is not in visited
        if node not in visited:
            # create new node
            new_node = Node(node.val, [])

            # add new node to visited
            visited[node] = new_node

            # iterate through neighbors
            for neighbor in node.neighbors:
                # call dfs on neighbor
                new_neighbor = self.dfs(neighbor, visited)

                # add new neighbor to new node's neighbors
                new_node.neighbors.append(new_neighbor)

        # return node
        return visited[node]

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.cloneGraph([2,7,11,15], 9)
    print(answer)

if __name__ == '__main__':
    main()


