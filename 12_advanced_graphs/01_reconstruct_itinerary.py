#!/usr/bin/env python

# RECONSTRUCT ITINERARY
#
# - given list of itinerary pairs (which are our graph edges)
# - job is to create itinerary of stops using each ticket exactly once
# - if more than one answer available, provided the one that comes first in sorted alphabetical order (smallest lexical order)
#
# NOTES
#
# - solution uses DFS to do GRAPH TRAVERSAL
# - solution uses ADJACENCY LIST
#
# - left side of adjaceny list is list of unique airports (this is a HASHMAP)
# - right side is names of airports that we fly to from each of the corresponding left side airports in sorted order
# - start with JFK
#     - go to first one in list and cross it off while adding it to our results list (these are our nodes)
# - note that length of results array when you are done is equal to the number of tickets plus 1 (the tickets are the edges - plus one because you account for the starting node, in this case JFK)
# - go down to row for airport that you just crossed off above and continue to do the same until you go through all of them
# - note that when you are traversing solutions, you may come across solutions that don't work in which case you will need to BACKTRACK
# - TIME COMPLEXITY O(E)^2 # where E is number of edges
# - MEMORY COMPLEXITY O(E) # where E is number of edges


import argparse
from typing import List

class Solution:

            def findItinerary(self, tickets: List[List[str]]) -> List[str]:
                # create adjacency list
                adj_list = {}

                # create results list
                results = []

                # populate adjacency list
                for ticket in tickets:
                    if ticket[0] not in adj_list:
                        adj_list[ticket[0]] = []
                    adj_list[ticket[0]].append(ticket[1])

                # sort adjacency list
                for key in adj_list:
                    adj_list[key].sort()

                # call helper function
                self.dfs(adj_list, 'JFK', results)

                # reverse results list
                results.reverse()

                # return results list
                return results

            def dfs(self, adj_list, airport, results):
                # while airport is in adjacency list
                while airport in adj_list and adj_list[airport]:
                    # get next airport
                    next_airport = adj_list[airport].pop(0)

                    # call dfs on next airport
                    self.dfs(adj_list, next_airport, results)

                # add airport to results list
                results.append(airport)


def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
    print(answer)

if __name__ == '__main__':
    main()


