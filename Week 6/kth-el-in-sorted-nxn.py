"""
heap solution:
runtime: based on num of times we push/pop largest possible queue size, so O(klogN)
space: O(N)
example from mock:
124
356
789
"""
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        queue = [(matrix[0][0], 0,0)]
        seen = set()
        seen.add((0,0))
        dirs = [[0,1], [1,0]] # right and down
        while queue: # queue: [2, 3]
            currInt, r, c = heapq.heappop(queue)
            if k == 1:
                return currInt # return
            k -= 1
            for dx, dy in dirs:
                row, col = dx+r, dy+c
                if row >= 0 and col >= 0 and row < n and col < n and (row, col) not in seen:
                    seen.add((row, col))
                    heapq.heappush(queue, (matrix[row][col], row, col))

    def kthSmallestBinary(self, matrix:List[List[int]],k:int) -> int:
        """
        after looking at the solution for binary search, im not a fan of how many times we have to
        process each element over and over until we get our value, but it does help the code look
        a bit cleaner
        time: O(N log(max-min))
        space: O(1)
        """
        n=len(matrix)
        lo,hi=matrix[0][0],matrix[n-1][n-1]
        while lo != hi:
            mid = (lo+hi) // 2
            count = 0
            r,c=n-1,0
            while r >= 0 and c < n:
                if matrix[r][c] <= mid:
                    count += r+1
                    c += 1
                else:
                    r -= 1
            if count >= k:
                hi = mid
            else:
                lo = mid+1
        return hi
if __name__ == "__main__":
    cases = [
        [[[1,5,9],[10,11,13],[12,13,15]],8],
        [[[-5]],1],
    ]
    s=Solution()
    for matrix, k in cases:
        print(s.kthSmallestBinary(matrix, k))
