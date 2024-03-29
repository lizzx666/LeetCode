'''


Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.


Example 1:
Input: root = [4,2,6,1,3]
Output: 1


Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        cur = root
        pre = None
        result = float('inf')

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre:
                    result = min(result,abs(cur.val-pre.val))
                pre = cur
                cur = cur.right
        return result 
