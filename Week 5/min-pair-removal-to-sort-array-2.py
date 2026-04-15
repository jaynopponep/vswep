class Node:
    def __init__(self, val, idx, left=None, right=None, deleted=False):
        self.val = val
        self.idx = idx
        self.left = left
        self.right = right
        self.deleted = deleted
    def __lt__(self, other):
        # apparently, if we write a __lt__ function, heapq auto identifies it, and uses
        # it for understanding how to compare nodes since theyre a custom class 
        return self.idx < other.idx

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        prev = None
        sumMinHeap = []
        unsortedRel = 0
        ops = 0
        heapq.heapify(sumMinHeap)
        for i, num in enumerate(nums):
            newNode = Node(num, i)
            newNode.left = prev
            if prev:
                prev.right = newNode
            if (i-1) >= 0:
                prevNum, currNum = nums[i-1], nums[i]
                heapq.heappush(sumMinHeap, (prevNum+currNum, prev, newNode))
                if prevNum > currNum:
                    unsortedRel += 1
            prev = newNode
        prev.right = None
        while unsortedRel != 0:
            currSum, leftNode, rightNode = heapq.heappop(sumMinHeap)
            if leftNode.deleted or rightNode.deleted:
                continue
            leftNode.deleted = True
            rightNode.deleted = True
            if leftNode.left and leftNode.left.val > leftNode.val:
                unsortedRel -= 1
            if leftNode.val > rightNode.val:
                unsortedRel -= 1
            if rightNode.right and rightNode.val > rightNode.right.val:
                unsortedRel -= 1
            mergedNode = Node(currSum, leftNode.idx)
            mergedNode.left, mergedNode.right = leftNode.left, rightNode.right
            if mergedNode.left:
                mergedNode.left.right = mergedNode
            if mergedNode.right:
                mergedNode.right.left = mergedNode
            if mergedNode.left and mergedNode.left.val > mergedNode.val:
                unsortedRel += 1
            if mergedNode.right and mergedNode.val > mergedNode.right.val:
                unsortedRel += 1
            if leftNode.left:
                heapq.heappush(sumMinHeap, (currSum+mergedNode.left.val, leftNode.left, mergedNode))
            if rightNode.right:
                heapq.heappush(sumMinHeap, (currSum+mergedNode.right.val, mergedNode, rightNode.right))
            ops += 1
        return ops
