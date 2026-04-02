# below uses a DFS way, which feels more natural than BFS which follows
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0]) # based on constraints (m=height,n=width)
        # higher level iteration to mark "unsurroundable"
        flagged = set()
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs_flag(row, col):
            flagged.add((row, col))
            for dr, dc in dirs:
                r,c=dr+row,dc+col
                if r >= 0 and c >= 0 and r < m and c < n and (r,c) not in flagged and board[r][c] == "O":
                    dfs_flag(r, c)
        # left and right column
        for i in range(m):
            if board[i][0] == "O":
                dfs_flag(i, 0)
            if board[i][n-1] == "O":
                dfs_flag(i, n-1)
        # top and bottom row
        for j in range(n):
            if board[0][j] == "O":
                dfs_flag(0,j)
            if board[m-1][j] == "O":
                dfs_flag(m-1, j)
        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == "O" and (i,j) not in flagged:
                    board[i][j] = "X"

# the "BFS" way, which isn't too different.:
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import deque
        m,n=len(board),len(board[0]) # based on constraints (m=height,n=width)
        # higher level iteration to mark "unsurroundable"
        flagged = set()
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        def bfs(row, col):
            flagged.add((row, col))
            queue = deque()
            queue.append((row, col))
            while queue:
                length = len(queue)
                for i in range(length):
                    row, col = queue.popleft()
                    for dr, dc in dirs:
                        r,c=dr+row,dc+col
                        if r >= 0 and c >= 0 and r < m and c < n and (r,c) not in flagged and board[r][c] == "O":
                            flagged.add((r, c))
                            queue.append((r,c))
        # left and right column
        for i in range(m):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][n-1] == "O":
                bfs(i, n-1)
        # top and bottom row
        for j in range(n):
            if board[0][j] == "O":
                bfs(0,j)
            if board[m-1][j] == "O":
                bfs(m-1, j)
        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == "O" and (i,j) not in flagged:
                    board[i][j] = "X"
        
