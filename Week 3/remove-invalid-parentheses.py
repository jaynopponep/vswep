class Solution:
    """
    first ideas would be having a (very costly) valid parentheses helper
    for each time we remove a parentheses to see if it becomes valid.
    if valid -> push to 'res'. if not -> continue searching from that
    state after removing that specific parentheses
    ()())(), if removing idx=0, )())() branches to ())() for ones that
    follow removing first index first
    we want the MINIMUM # of parentheses removed, so not every valid path
    will go into result. once we find any 1 path that is valid at that
    instant, all the other valids from that BFS level will be a part of res
    in other words, no point exploring deeper into the paths. 
    specifically no need for DFS since we'd be searching for unnecessary valid
    strings
    """
    from typing import List
    def removeInvalidParentheses(self, s: str) -> List[str]:
        from collections import deque
        def isValid(str):
            openParens = 0
            for c in str:
                if c == "(":
                    openParens += 1
                elif c == ")":
                    if openParens == 0:
                        return False
                    openParens -= 1
            return openParens == 0
        queue = deque()
        queue.append(s)
        visited = {s}
        found = False
        res = []
        if isValid(s):
            return [s]
        while not found:
            queueSize = len(queue)
            for _ in range(queueSize):
                string = queue.popleft()
                for i in range(len(string)):
                    curr = string[:i] + string[i+1:]
                    if curr in visited:
                        continue
                    if isValid(curr):
                        found = True
                        if found:
                            res.append(curr)
                    else:
                        queue.append(curr)
                    visited.add(curr)
        return res if found else [""]


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        "()())()",
        "(a)())()",
        ")(",
        "n",
    ]
    for case in test_cases:
        print(s.removeInvalidParentheses(case))
