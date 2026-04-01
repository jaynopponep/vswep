from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        scheduleMap = defaultdict(list) # treat pre-reqs as a directed graph
        # if a course between 0 and numCourses-1 (incl) isn't mentioned:
        # then it has no prereqs
        for course, prereq in prerequisites:
            scheduleMap[prereq].append(course)
        globalSeen = set()
        # recursive call to make sure there is no cycle within a directed path
        def traverse(x):
            nonlocal globalSeen
            if x not in scheduleMap:
                # course x has no prereqs!
                return True
            if x in globalSeen:
                # bad, cycle found
                return False
            globalSeen.add(x)
            for dst in scheduleMap[x]:
                if not traverse(dst):
                    return False
            scheduleMap[x] = [] # probing to avoid repeated traversals
            globalSeen.remove(x)
            return True
        for i in range(numCourses):
            if scheduleMap[i]:
                if not traverse(i):
                    return False
        return True

if __name__ == "__main__":
    test_cases = [
        [2, [[1,0]]], # T
        [2, [[1,0], [0,1]]], # F 
        [5, [[1,4], [2,4], [3,1], [3,2]]] # T
    ]
    s = Solution()
    for numCourses, prerequisites in test_cases:
        print(s.canFinish(numCourses, prerequisites))
