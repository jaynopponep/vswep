class Solution:
    """
    - lengths of s1 and s2 == n
    - (a-z only)
    logic/rules:
    - i < j AND (j-i) % 2 == 0
    general:
    reminds me abit of interleaving string sort of
    examples take s1 and try to turn it into s2
    ideas:
    - dfs/bfs paths until we find one that yields something matching s2
    - we could memoize invalid paths previously entered to save time
    - we can never swap an even index with an odd index, so there are
    two subproblems, if we can match the even indices AND the odd indices.
    - i < j actually seems to not restrict anything. char at idx 0 can 
    always move up by 2, 4, ... and idx 8 can move down to 0. 
    - since that's possible, all we really need is a freq map or Counter()
    to compare with s2 and that's about it
    """
    def checkStrings(self, s1: str, s2: str) -> bool:
        from collections import Counter
        n=len(s1) #also len(s2)
        # n is atleast length 1
        if n==1:
            return s1 == s2
        even = Counter(s1[::2]) == Counter(s2[::2]) # every two index start from 0
        odd = Counter(s1[1::2]) == Counter(s2[1::2]) # start from 1 (odd)
        return even and odd

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        ["abcdba", "cabdab"], # t
        ["abe", "bea"], # f
    ]
    for s1, s2 in test_cases:
        print(s.checkStrings(s1,s2))
