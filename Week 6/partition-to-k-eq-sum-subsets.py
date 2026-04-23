from typing import List

"""
it's clear that we do backtracking here, but I definitely had to do some searching which led me to learn what bitmask even was.
this is the crucial component to make it easy and efficient to check the "state" of our seen indices/numbers to eliminate subproblems.
mask | (1 << j) is basically setting the current index j to seen (e.g. j = 2 -> 000100)
mask ^ (1 << j) reverts that (000100 -> 000000)
mask & (1 << j) uses 'and' to check if proposed bit (1 << j) returns a truthy value when && with current mask
"""

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        n=len(nums)
        mask = 0
        memo = {}
        def dp(currSum):
            nonlocal mask
            if mask == (1 << n) - 1:
                # e.g. if n == 4, (1 << n) -> 10000, a complete mask would be 01111, their difference is 1.
                return True
            if mask in memo:
                return memo[mask]
            if currSum == target:
                currSum = 0
            for j in range(0,n):
                if not mask & (1 << j):
                    if currSum + nums[j] <= target:
                        mask = mask | (1 << j)
                        if dp(currSum + nums[j]):
                            return True
                        mask = mask ^ (1 << j)
            memo[mask] = False
            return False
        return dp(0) # sum

if __name__ == "__main__":
    s = Solution()
    cases = [
        [[4,3,2,3,5,2,1], 4],
        [[1,2,3,4], 3],
    ]
    for nums, k in cases:
        print(s.canPartitionKSubsets(nums, k))
