"""
good trail: as long as possible + even, gradual, uphill slope (always increase by 1 each step)
valid hiking trail: starts at 0, ends at 9
trailhead: always height 0, or where a trail (or multiple trails) begins
"." represents impassable tiles.
no diagonals, Up Down Left Right only.
direct 0 to 9 is not allowed. must be 0, 1, 2, 3, 4... 9
"""

trails = []
file_name = 'aoc-day10-data.txt'
#file_name = 'aoc-day10-data-easy.txt'
with open(file_name, 'r') as f:
    # to have our input pretty clean, we should have each num be 
    # individual elements. so a 2d matrix.
    for line in f:
        trails.append(list(line.strip()))

def findTrails(hikingTrail):
    m, n = len(trails), len(trails[0]) # m=height, n=width
    totalTrails = 0
    dirs = [[0,1],[1,0],[-1,0],[0,-1]]

    def dfs(row, col, curr, seen):
        nonlocal totalTrails
        if curr == "9":
            if (row, col) not in seen:
                seen.add((row, col))
                totalTrails += 1
            return
        for dx, dy in dirs:
            r,c=dx+row,dy+col
            if r >= 0 and c >= 0 and r < m and c < n and trails[r][c] != '.' and (int(trails[r][c]) == int(curr) + 1):
                dfs(r, c, trails[r][c], seen)
        return
    
    def dfs_part2(row, col, curr):
        nonlocal totalTrails
        if curr == "9":
            totalTrails += 1
            return
        for dx, dy in dirs:
            r,c=dx+row,dy+col
            if r >= 0 and c >= 0 and r < m and c < n and trails[r][c] != '.' and (int(trails[r][c]) == int(curr) + 1):
                dfs_part2(r, c, trails[r][c])
        return

    for i in range(m):
        for j in range(n):
            if trails[i][j] == "0":
                # i think DFS would make sense here, but BFS is ok too
                #dfs(i, j, "0", set())
                dfs_part2(i,j,"0")
    return totalTrails

if __name__ == "__main__":
    print(findTrails(trails))
