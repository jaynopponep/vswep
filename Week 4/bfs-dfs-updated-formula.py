"""
below i address both graphs and trees. let's say all of them use a
node as a data structure.
"""

def bfs(root):
    from collections import deque
    queue = deque()
    queue.append(root)
    visited = set()
    while queue:
        length = len(queue)
        for i in range(length):
            curr = queue.popleft()
            process(curr)
            for nei in curr.neighbors:
                # assume trees' children will be represented as neighbors
                if nei not in visited:
                    queue.append(nei)
                    visited.add(nei)
    done

def dfs_iter(root):
    stack = []
    stack.append(root)
    visited = set()
    while stack:
        curr = stack.pop()
        process(curr)
        for nei in curr.neighbors:
            if nei not in visited:
                stack.append(nei)
                visited.add(nei)
    done

def func():
    def dfs(root, seen):
        seen.add(root) # <- really position of this can depend on our goal
        if valid(root): # arbitrary validation func
            process(root)
            return
        for nei in root.neighbors:
            if nei not in seen:
                dfs(nei, seen)
        done
    dfs(root, set())

