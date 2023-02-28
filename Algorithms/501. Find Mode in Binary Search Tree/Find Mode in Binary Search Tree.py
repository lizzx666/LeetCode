'''


Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [1,null,2,2]
Output: [2]


Example 2:
Input: root = [0]
Output: [0]


'''






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        pre = None
        count = 0
        max_count = 0
        result = []
        stack = []

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre == None:
                    count = 1
                elif pre.val == cur.val:
                    count+=1
                else:
                    count = 1
                pre = cur
                if count == max_count:
                    result.append(cur.val)
                if count > max_count:
                    max_count = count
                    result = []
                    result.append(cur.val)
                
                cur = cur.right
        return result


