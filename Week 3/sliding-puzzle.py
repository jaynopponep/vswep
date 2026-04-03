# i generated below with Claude
puzzle_2x2_hard = [
    [3, 1],
    [2, 0]
]

puzzle_2x2_hard_goal = [
    [1, 2],
    [3, 0]
]

puzzle_3x3_medium = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]  # two moves from solved
]

puzzle_3x3_hard = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

puzzle_3x3_hard_goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
"""
- What values will you use within your board? 
-> Integer values, 0 represents empty tile
- How will you represent the goal state?
-> having the 0 end up at [m-1][n-1] where m = height, n = width
and that all numbers from left to right, top to bottom, are in consecutive order. 
e.g. puzzle_3x3_hard would be:
[1,2,3],
[4,5,6],
[7,8,0]
- How will you represent the empty space?
-> 0
- How will you keep track of your visited nodes? Remember that lists can't be used as the keys of hash maps.
-> each node is actually an entire state of the board, but represented as a tuple of tuples since we lists are not hashable
- How will you find the neighbors for a particular node?
-> Only thing we can move are what's adjacent (no diagonal) to the
empty tile. so find empty tile -> explore all paths of whether to move *from* above, left, right, below
"""

def solve_puzzle(puzzle_board, goal):
    seen = set()
    m,n=len(puzzle_board), len(puzzle_board[0])
    dirs = [[0,1],[1,0],[-1,0],[0,-1]]
    def find_empty_tile(board): # -> returns tuple (i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)
        return None
    def dfs(curr_board):
        for row in curr_board:
            print(row)
        print("----")
        if curr_board == goal:
            return True
        seen.add(tuple(tuple(row) for row in curr_board))
        x,y = find_empty_tile(curr_board)
        for dx, dy in dirs:
            r, c = x+dx, y+dy
            if r >= 0 and c >= 0 and r < m and c < n:
                edited_board = [row[:] for row in curr_board]
                edited_board[x][y], edited_board[r][c] = edited_board[r][c], edited_board[x][y]
                if tuple(tuple(row) for row in edited_board) not in seen:
                    if dfs(edited_board):
                        return True # having these t/f just so it can properly stop finding a path
        return False
    dfs(puzzle_board)

if __name__ == "__main__":
    print(solve_puzzle(puzzle_3x3_hard, puzzle_3x3_hard_goal))
    print("----")
    print(solve_puzzle(puzzle_2x2_hard, puzzle_2x2_hard_goal))
