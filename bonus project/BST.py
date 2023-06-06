class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, node):
        # Insert a node into the tree based on its value
        if self.value < node.value:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
        else:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)

    def find_first_larger_node(self, target):
        first_larger = None
        current = self
        while current:
            # Traverse the tree until a node with a value greater than the target is found
            if current.value > target:
                first_larger = current.value
                current = current.left
            else:
                current = current.right
        return first_larger


def main():
    # Create a tree with a root node
    root = Node(20)
    node_values = [9, 5, 12, 11, 14, 25]
    
    # Insert nodes into the tree
    for value in node_values:
        root.insert(Node(value))

    target_node = 14
    
    # Find the first larger node in the tree relative to the target node
    first_larger = root.find_first_larger_node(target_node)

    # Define colors for output statements
    color_cyan = "\033[1;36m"  # Cyan color
    color_yellow = "\033[1;33m"  # Yellow color
    color_reset = "\033[0m"  # Reset color to default

    # Print colored output
    print(f"{color_yellow}First larger node: {color_cyan}{first_larger}{color_reset}")


if __name__ == "__main__":
    main()
