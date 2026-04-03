"""
from my understanding, BFS is only applicable iteratively and not recursively. 
below are how I usually see Bfs/dfs and how I approach the usages
"""

# let's say for below, we have a tree
def bfs(root):
    from collections import deque
    queue = deque()
    queue.append(root) # init with "first layer" of BFS, which is just the root
    while queue: # continue until all nodes or elements exhausted, or visited
        length = len(queue) # prep to iterate the size of the current queue
        for i in range(length):
            curr = queue.popleft() # extract the current node or element
            process(curr) # do whatever is needed to current node
            for neighbor in curr.neighbors: # let's say each node has neighbors attribute
                queue.append(neighbor)
    done

# rather than a deque/queue, we use a stack
def dfs_iter(root):
    stack = []
    stack.append(root) # init first node or element
    while stack:
        curr = stack.pop()
        process(curr)
        for neighbor in curr.neighbors:
            stack.append(neighbor)
    done

def dfs_rec(root):
    if root == good:
        process(root)
    seen.add(root)
    for neighbor in root.neighbors:
        if neighbor not in seen:
            dfs_rec(neighbor)
    done
