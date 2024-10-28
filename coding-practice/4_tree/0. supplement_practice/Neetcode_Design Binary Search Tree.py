from typing import List


class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = self.insert_helper(self.root, key, val)

    def insert_helper(self, node, key, val) -> TreeNode:
        if not node:
            return TreeNode(key, val)

        if key < node.key:
            node.left = self.insert_helper(node.left, key, val)
        elif key > node.key:
            node.right = self.insert_helper(node.right, key, val)
        else:
            node.val = val
        
        return node
                
    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if curr.key < key:
                curr = curr.right
            elif curr.key > key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        return self.find_min_node(self.root).val

    def find_min_node(self, node) -> TreeNode:
        curr = node
        while curr.left:
            curr = curr.left
        return curr

    def getMax(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.right:
            curr = curr.right

        return curr.val

    def remove(self, key: int) -> None:
        self.root = self.remove_helper(self.root, key)
    
    def remove_helper(self, node, key) -> TreeNode:
        if not node:
            return None
            
        if key < node.key:
            node.left = self.remove_helper(node.left, key)
        elif key > node.key:
            node.right = self.remove_helper(node.right, key)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                successor = self.find_min_node(node.right)
                node.key = successor.key
                node.val = successor.val

                node.right = self.remove_helper(node.right, successor.key)   
        return node

    def getInorderKeys(self) -> List[int]:
        self.lst = []
        self.dfs_helper(self.root)

        return self.lst

    def dfs_helper(self, node):
        if not node:
            return
        
        self.dfs_helper(node.left)
        self.lst.append(node.key)
        self.dfs_helper(node.right)