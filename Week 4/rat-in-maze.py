class Solution:
    def ratInMaze(self, maze):
        m, n = len(maze), len(maze[0]) # height, width
        res = []
        dirs = {(1,0): "D", (0,-1): "L", (0,1): "R", (-1,0): "U"}
        # sorting the key/vals above this way makes it so we automatically consider lexicographically
        # otherwise, we'd return sorted(res) at the end.
        seen = set()
        def dfs(row, col, curr):
            if row == m-1 and col == n-1:
                res.append(curr)
                return
            seen.add((row, col))
            for (dx,dy), direction in dirs.items():
                r,c=row+dx,col+dy
                if (r >= 0 and c >= 0 and r < m and c < n and 
                (r, c) not in seen and maze[r][c] == 1):
                    dfs(r,c,curr+direction)
            seen.remove((row, col))
            return
        dfs(0,0,"")
        return res

if __name__ == "__main__":
    cases = [
        [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]],
        [[1, 0], [1, 0]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    ]
    s = Solution()
    for case in cases:
        print(s.ratInMaze(case))
