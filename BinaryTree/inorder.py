# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recur(self,node,arr):
        if node == None:
            return
        else:
            self.recur(node.left,arr)
            arr.append(node.val)
            self.recur(node.right,arr)
    
    def inorderTraversal(self, root):
        arr = []
        self.recur(root,arr)
        
        return arr
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        