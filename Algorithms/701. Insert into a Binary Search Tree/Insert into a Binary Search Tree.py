'''


You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



#递归法
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val)
            return node
        
        if root.val>val:
            root.left = self.insertIntoBST(root.left,val)
        if root.val<val:
            root.right = self.insertIntoBST(root.right,val)
        
        return root


#迭代法
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val)
            return node

        cur = root
        parent = root

        while cur:
            parent = cur
            if cur.val>val:
                cur = cur.left
            else:
                cur = cur.right
        
        node = TreeNode(val)
        if val < parent.val:
            parent.left = node
        else:
            parent.right = node
        return root
