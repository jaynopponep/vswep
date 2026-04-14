from typing import List
from collections import defaultdict
import heapq

"""
high level dijkstras:
- must have a neighboring map listed as {src: [(cost, dst), (cost2, dst2), ...]}
- minHeap auto picks optimal routes. whichever (cost, dst) pair gets to visited first is the most optimal.
- at the current popped item, we look at each neighbor, a little similar to Bfs. but we must add our current cost
onto that neighbor, before it goes into the heap.
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        networkMap = defaultdict(list)
        visited = {}
        # network map tracks as src: [(cost, dst), (cost, dst)]
        # visited tracks visited nodes associated with their costs {(dst, cost), ...}
        minHeap = [(0,k)]
        heapq.heapify(minHeap)
        for src, dst, cost in times:
            networkMap[src].append((cost, dst))
        while minHeap:
            currCost, currNode = heapq.heappop(minHeap)
            if currNode in visited:
                continue
            visited[currNode] = currCost
            for cost, nei in networkMap[currNode]:
                netCost = cost + currCost
                heapq.heappush(minHeap, (netCost, nei))
        if len(visited) != n:
            return -1
        return max(visited.values())

if __name__ == "__main__":
    s = Solution()
    cases = [
        [[[2,1,1],[2,3,1],[3,4,1]], 4, 2],
        [[[1,2,1]], 2, 1],
        [[[1,2,1]], 2, 2],
        [[[2,3,1], [2,1,2], [3,4,5], [1,5,5], [4,6,2], [4,5,1], [5,6,1]], 6, 2],
    ]
    for times, n, k in cases:
        print(s.networkDelayTime(times, n, k))
