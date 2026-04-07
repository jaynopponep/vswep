# simplified powerset problem without backtracking:

def powerset(listOfInts, k=None): # precond: assume k is always given. if not, return the full powerset
    powersetItems = [[]] # start with empty set
    res = []
    for num in listOfInts:
        subsets = []
        for preexistingSet in powersetItems:
            currSet = preexistingSet + [num]
            if k is None:
                subsets.append(currSet)
                res.append(currSet)
            elif len(currSet) < k:
                subsets.append(currSet)
            elif len(currSet) == k:
                res.append(currSet)
        powersetItems += subsets
    return res

def powerset_backtracking(listOfInts):
    res = []
    n = len(listOfInts)
    def backtrack(i, curr):
        if i == n: # exhausted all numbers
            res.append(curr)
            # we know we'll achieve all unique sets due to the take/skip and index exhaustion
            # which create non overlapping paths 
            return
        backtrack(i+1, curr + [listOfInts[i]]) # send a version where you add the curr value at i
        backtrack(i+1, curr)
    backtrack(0, [])
    return res

if __name__ == "__main__":
    tests = [
        [[1,2,3], None],
        [[1,2,3], 1],
        [[1,2,3], 2],
        [[1,2,3], 3],
    ]
    for ints, k in tests:
        print(powerset(ints, k))
