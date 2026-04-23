from typing import List
import heapq

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
        main challenges are handling multiple meetings at the same time stamp, cleaning up nodes,
        unioning in order of times starting at 0 so nodes do not "get a secret" before they are even shared
        -> initiate/union with nodes (0)-(firstPerson) connected (e.g. (0)-(1))
        -> build() checks if either node "already knows the secret". if so, both of them will know the secret,
        so we can set both their parents to 0 with union(0,X)
        -> "seen" will have a state for the current time stamp only. this is to cross ref if any of the
        unions were "successful", or able to get the secret. if not, set them as lone-nodes. if they were 
        successful nodes, they belong in thoseWhoKnow since they know the secret.
        """
        par = {}
        meetingHeap = []
        thoseWhoKnow = {0, firstPerson}
        for x,y,t in meetings:
            heapq.heappush(meetingHeap, (t,x,y))
        def find(x):
            if x not in par:
                par[x] = x
            if par[x] != par[par[x]]:
                par[x] = find(par[x])
            return par[x]
        def union(x,y): # main parent be px or x
            px,py = find(x), find(y)
            par[py] = px
        union(0, firstPerson)
        def build(a,b,currSet):
            currSet.add(a)
            currSet.add(b)
            if find(a) == 0 or find(b) == 0:
                union(0,a)
                union(0,b)
            else:
                union(a,b)
        while meetingHeap:
            seen = set()
            ft,fx,fy = heapq.heappop(meetingHeap)
            build(fx,fy,seen)
            while meetingHeap and meetingHeap[0][0] == ft:
                ct,cx,cy = heapq.heappop(meetingHeap)
                build(cx,cy,seen)
            for person in seen:
                if find(person) != 0:
                    par[person] = person
                else:
                    thoseWhoKnow.add(person)
        return list(thoseWhoKnow)
if __name__ == "__main__":
    cases = [
        [6, [[1,2,5],[2,3,8],[1,5,10]], 1],
        [4, [[3,1,3],[1,2,2],[0,3,3]], 3],
        [5, [[3,4,2],[1,2,1],[2,3,1]], 1],
        [5, [[1,4,3],[0,4,3]], 3],
    ]
    s = Solution()
    for n, meetings, firstPerson in cases:
        print(s.findAllPeople(n,meetings,firstPerson))
