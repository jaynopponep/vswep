"""
-> since examples show fragments & code without quotes, input should be ints
-> note we are only ever combining TWO fragments (pair), and not more than one
-> question is very similar to permutations backtracking problem I've done before, so I'll write a version of that to support >2 fragments and also write one
where we expect just a pair of fragments
"""

from typing import List
import time
# also adding time to compare run time of both of these versions

def num_combinations(fragments: List[int], accessCode: int) -> int:
    n = len(fragments)
    numCombos = 0
    for i in range(n):
        for j in range(n):
            if i != j and (str(fragments[i]) + str(fragments[j])) == str(accessCode):
                numCombos += 1
    return numCombos

# below example I wrote in a way to support >2 fragments
def num_combinations_v2(fragments: List[int], accessCode: int) -> int:
    numCombos = 0
    n = len(str(accessCode))
    def backtrack(idx, codeSoFar, seen):
        nonlocal numCombos
        if len(codeSoFar) > n:
            return
        if codeSoFar == str(accessCode):
            numCombos += 1
            return
        for i, fragment in enumerate(fragments):
            if i not in seen:
                seen.add(i)
                backtrack(i, codeSoFar + str(fragment), seen)
                seen.discard(i)
        return

    for i, fragment in enumerate(fragments):
        starting = set()
        starting.add(i)
        code = str(fragment)
        backtrack(i, code, starting)
    return numCombos

if __name__ == "__main__":
    cases = [
        [[1, 212, 12, 12], 1212], # expects: 3
        [[777, 7, 777, 77, 77], 7777], # expects: 6
        [[11, 11, 110], 11011] # expects: 2
    ]
    for fragment, code in cases:
        start = time.perf_counter()
        print(num_combinations(fragment, code))
        elapsed = (time.perf_counter() - start) * 1000
        print(f"v1: {elapsed:.3f}ms")
        start = time.perf_counter()
        print(num_combinations_v2(fragment, code))
        elapsed = (time.perf_counter() - start) * 1000
        print(f"v2: {elapsed:.3f}ms")
