"""
A-Z, a-z
input: dictionary/list of words
given the mechanics of this problem, let's say expected for len(dictionary) >= 2
so there's always going to be a comparison of two words.
output: list of chars
"""

"""
disect our example:
RAT & ART -> R and A differ first -> R comes before A
ART & CAT -> A and C differ first -> A comes before C
CAT & CAR -> C and C match -> A and A match -> T and R differ -> T comes before R
T comes before R, where R comes before A, where A comes before C
"""

"""
-> helper func for comparing two words, and mapping char1 -> char2 in hashmap, where
char1 comes before char2. (e.g. RAT vs ART -> {"R": ["A", ..., ....]}
-> iterate through each character starting from the second in dictionary. before vs. curr
-> had to be reminded what an in-degree was and how to take advantage of it here.
within a map, for key, values -> values += 1 for its in-degree count.
-> begin a queue (BFS) that accepts nodes where in-degree == 0, as in all prev nodes are processed.
-> each time we hit a new node, in-degree value -= 1, if 0 then add to queue.
"""

from collections import defaultdict, deque

wordOrderMap = defaultdict(list)
def helper_map(w1, w2):
    c1, c2 = 0, 0
    while w1[c1] == w2[c2]:
        c1 += 1
        c2 += 1
    wordOrderMap[w1[c1]].append(w2[c2])
    # no need to return anything

def extract_alphabet(dictionary):
    l=1
    while l < len(dictionary):
        before, curr = dictionary[l-1], dictionary[l]
        helper_map(before, curr)
        l+=1
    # expected: order map is created
    inDegree = {node: 0 for node in wordOrderMap}
    for key, valueArray in wordOrderMap.items():
        for value in valueArray:
            if value not in inDegree: # consider that final node does not appear in wordOrderMap
                inDegree[value] = 0
            inDegree[value] += 1
    queue = deque([zeroNode for zeroNode in inDegree if inDegree[zeroNode] == 0])
    res = []
    while queue:
        length = len(queue)
        for i in range(length):
            curr = queue.popleft()
            res.append(curr)
            for neighbor in wordOrderMap[curr]:
                if neighbor in inDegree:
                    inDegree[neighbor] -= 1
                    if inDegree[neighbor] == 0:
                        queue.append(neighbor)
    return res

if __name__ == "__main__":
    test_cases = [
        ["RAT", "ART", "CAT", "CAR"], # -> ["T","R","A","C"]
    ]
    for case in test_cases:
        print(extract_alphabet(case))
