from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par={} # 1: 1, 2: 1, 3: 1, 4: 1, 
        def find_parent(x):
            if x not in par:
                par[x] = x
            if par[x] != par[par[x]]:
                # this can occur when creating two separate graphs,
                # and then connecting them after.
                par[x] = find_parent(par[x])
            return par[x]
        
        def union(x, y):
            parx = find_parent(x)
            pary = find_parent(y)
            # need above to ensure parents are correct before unionizing anything
            if parx == pary: # redundant
                return False
            # par[y] = parx or par[pary] = x would risk incorrect assignment
            par[pary] = parx
            return True
        
        for a, b in edges:
            if not union(a,b):
                return [a,b]

if __name__ == "__main__":
    cases = [
        [[16,25],[7,9],[3,24],[10,20],[15,24],[2,8],[19,21],[2,15],[13,20],[5,21],[7,11],[6,23],[7,16],[1,8],[17,20],[4,19],[11,22],[5,11],[1,16],[14,20],[1,4],[22,23],[12,20],[15,18],[12,16]],
        [[1,5],[3,4],[3,5],[4,5],[2,4]],
        [[1,2],[2,3],[3,4],[1,4],[1,5]],
    ]
    s = Solution()
    for edges in cases:
        print(s.findRedundantConnection(edges))
