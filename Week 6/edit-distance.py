"""
key things here:
- calculating the number of operations just means calculating the cost of either insert/del/replacing each letter
based on whether each index matches or not with 2 pointers
- we consider all decisions/paths, but get to base each "step" as (idx of word1, idx of word2)
- each time both idxs match, our cost at the moment is 0 + the rest of the path (memoized)
- in all other cases, the current cost is 0.
- base cases: if we exhaust word2, then the rest of word1 is the rest of the cost + current cost
similarly: if we exhaust the first word, then the rest of word2 is the rest of the cost + current cost
"""

# top down memo approach:
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        m,n=len(word1),len(word2)
        ops = float('inf')
        def dfs(x, y):
            if x >= m:
                return n-y
            if y == n:
                return m-x
            if (x,y) in memo:
                return memo[(x,y)]
            skip = 1+ dfs(x+1,y)
            matched = dfs(x+1,y+1) + (0 if word1[x] == word2[y] else 1)
            insert = 1+dfs(x,y+1)
            memo[(x,y)]= min(skip, matched, insert)
            return memo[(x,y)]
        return dfs(0, 0)
        #runtime: theres (mxn) unique states, so runtime sits around O(mxn)
        #space: memo uses O(mxn) space

    # bottom up:
    def minDistanceBottomUp(self, word1: str, word2: str) -> int:
        """
        - its pretty satisfying drawing out the tabulation for this problem, which is expected to start
        out something like:
            h  o  r  s  e  ""
        r  [ ][ ][ ][ ][ ][3]
        o  [ ][ ][ ][ ][ ][2]
        s  [ ][ ][ ][ ][ ][1]
        "" [5][4][3][2][1][0]
        - representing the base case when each word is exhausted.
        - then we just start from bottom right to top left, and add up the current grid,
        determined by whether the letters match (match=0,no-match=1) + min(right, bottom, bottom-right)
            h  o  r  s  e  ""
        r  [3][3][2][3][3][3]
        o  [3][2][2][2][2][2]
        s  [4][3][2][1][1][1]
        "" [5][4][3][2][1][0]
        - then, memo[0][0] = 3 -> result
        """
        m,n=len(word1),len(word2)
        memo = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n,-1,-1): # i == 3,2,1,0
            for j in range(m,-1,-1): # j = 5,4,3,2,1,0
                if i==n and j==m:
                    continue
                if i == n:
                    memo[i][j] = m-j
                    continue
                if j == m:
                    memo[i][j] = n-i
                    continue
                cost = 0
                if word1[j] != word2[i]:
                    cost = 1
                memo[i][j] = min(1+memo[i+1][j],cost+memo[i+1][j+1],1+memo[i][j+1])
        return memo[0][0]
        # runtime: still O(mxn)
        # space: grid like shown above shows memo is O(mxn) space


if __name__ == "__main__":
    cases = [
        ["horse", "ros"],
        ["intention", "execution"],
        ["a", "aa"],
    ]
    s = Solution()
    for word1, word2 in cases:
        print(s.minDistanceBottomUp(word1, word2)) 
