class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreePractice:

    # Exercise 1: In-order Traversal (left-root-right)
    def inorder_traversal(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 2: Pre-order Traversal (root-left-right)
    def preorder_traversal(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 3: Post-order Traversal (left-right-root)
    def postorder_traversal(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 4: Level-order Traversal (BFS)
    def level_order_traversal(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 5: Find Maximum Element
    def find_max(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 6: Find Minimum Element
    def find_min(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 7: Find Height of Binary Tree
    def find_height(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 8: Count the Number of Nodes
    def count_nodes(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 9: Find the Sum of All Nodes
    def sum_of_nodes(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 10: Check if Two Trees are Identical
    def are_identical(self, root1, root2):
        # TODO: Fill in the logic
        pass

    # Exercise 11: Check if Binary Tree is Balanced
    def is_balanced(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 12: Find Lowest Common Ancestor (LCA)
    def find_lca(self, root, p, q):
        # TODO: Fill in the logic
        pass

    # Exercise 13: Check if Binary Tree is a Binary Search Tree (BST)
    def is_bst(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 14: Find the Diameter of the Binary Tree
    def find_diameter(self, root):
        # TODO: Fill in the logic
        pass

    # Exercise 15: Check if Tree is Symmetric
    def is_symmetric(self, root):
        # TODO: Fill in the logic
        pass

# Helper functions to create trees
def create_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

def create_another_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    return root

# Test cases
def run_tests():
    practice = TreePractice()
    sample_tree = create_sample_tree()
    another_sample_tree = create_another_sample_tree()

    # Test inorderTraversal
    print("Exercise 1: In-order Traversal")
    assert practice.inorder_traversal(sample_tree) == [4, 2, 5, 1, 6, 3, 7]

    # Test preorderTraversal
    print("Exercise 2: Pre-order Traversal")
    assert practice.preorder_traversal(sample_tree) == [1, 2, 4, 5, 3, 6, 7]

    # Test postorderTraversal
    print("Exercise 3: Post-order Traversal")
    assert practice.postorder_traversal(sample_tree) == [4, 5, 2, 6, 7, 3, 1]

    # Test levelOrderTraversal
    print("Exercise 4: Level-order Traversal")
    assert practice.level_order_traversal(sample_tree) == [1, 2, 3, 4, 5, 6, 7]

    # Test findMax
    print("Exercise 5: Find Maximum Element")
    assert practice.find_max(sample_tree) == 7

    # Test findMin
    print("Exercise 6: Find Minimum Element")
    assert practice.find_min(sample_tree) == 1

    # Test findHeight
    print("Exercise 7: Find Height")
    assert practice.find_height(sample_tree) == 3

    # Test countNodes
    print("Exercise 8: Count the Number of Nodes")
    assert practice.count_nodes(sample_tree) == 7

    # Test sumOfNodes
    print("Exercise 9: Find the Sum of All Nodes")
    assert practice.sum_of_nodes(sample_tree) == 28

    # Test areIdentical
    print("Exercise 10: Check if Two Trees are Identical")
    assert practice.are_identical(sample_tree, another_sample_tree) == False

    # Test isBalanced
    print("Exercise 11: Check if Binary Tree is Balanced")
    assert practice.is_balanced(sample_tree) == True

    # Test findLCA
    print("Exercise 12: Find Lowest Common Ancestor (LCA)")
    assert practice.find_lca(sample_tree, sample_tree.left.left, sample_tree.left.right).val == 2

    # Test isBST
    print("Exercise 13: Check if Binary Tree is a BST")
    assert practice.is_bst(sample_tree) == False

    # Test findDiameter
    print("Exercise 14: Find the Diameter of the Binary Tree")
    assert practice.find_diameter(sample_tree) == 4

    # Test isSymmetric
    print("Exercise 15: Check if Tree is Symmetric")
    assert practice.is_symmetric(sample_tree) == False

    print("All tests passed!")

# Run the tests
if __name__ == "__main__":
    run_tests()