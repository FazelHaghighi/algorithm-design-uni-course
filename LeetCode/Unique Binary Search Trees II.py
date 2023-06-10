class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        
        def generate(l: int, r: int) -> List[TreeNode]:
            if l == r:
                return [None]
            
            nodes = []
            for i in range(l, r):
                for lchild in generate(l, i):
                    for rchild in generate(i + 1, r):
                        node = TreeNode(i + 1)  # +1 to convert the index to the actual value
                        node.left = lchild
                        node.right = rchild
                        nodes.append(node)
            
            return nodes
        
        return generate(0, n)
