import sys
import re

# Binary Search Tree Implementation in Python
class BinarySearchTree:
    class _TreeNode:
        # Inner class to represent a tree node
        def __init__(self, key):
            self.key = key
            self.count = 1
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if root is None:
            return self._TreeNode(key)
        
        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)
        else:
            root.count += 1
        return root

    def inorder(self):
        print("Starting in-order traversal...")
        self._inorder_rec(self.root)
        print("In-order traversal completed.")

    def _inorder_rec(self, root):
        if root:
            self._inorder_rec(root.left)
            print(f"{root.key}: {root.count}")
            self._inorder_rec(root.right)


def main():
    # Check for command-line arguments for the file name
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        # Prompt the user for the file name if no command-line argument is provided
        file_name = input("Enter the filename: ")

    # Initialize BinarySearchTree
    bst = BinarySearchTree()
    
    try:
        with open(file_name, 'r') as file:
            word_count = 0
            for line in file:
                # Clean up and split words using regex, removing non-alphabetic characters
                words = re.findall(r'\b[a-zA-Z]+\b', line.lower())
                for word in words:
                    bst.insert(word)
                    word_count += 1
            print(f"Total words processed: {word_count}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        sys.exit(2)

    # Perform an in-order traversal of the Binary Search Tree
    bst.inorder()


if __name__ == "__main__":
    main()
