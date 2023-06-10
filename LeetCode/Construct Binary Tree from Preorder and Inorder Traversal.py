class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.buildTreeHelper(0, 0, len(inorder) - 1, preorder, inorder)

    def buildTreeHelper(self, preStart: int, inStart: int, inEnd: int, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preStart > len(preorder) - 1 or inStart > inEnd:
            return None
        
        root = TreeNode(preorder[preStart])
        inIndex = inorder.index(root.val)
        
        root.left = self.buildTreeHelper(preStart + 1, inStart, inIndex - 1, preorder, inorder)
        root.right = self.buildTreeHelper(preStart + inIndex - inStart + 1, inIndex + 1, inEnd, preorder, inorder)
        
        return root
