# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        
        res = []
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if not node:
                res.append("None")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return ",".join(res)

# TC O(n)
# SC O(n) # res list


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(",")
        
        if lst[0] == "None":
            return None
        
        root = TreeNode(int(lst[0]))
        
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            
            if lst[index] != "None":
                node.left = TreeNode(int(lst[index]))
                queue.append(node.left)
            
            index += 1
            
            if lst[index] != "None":
                node.right = TreeNode(int(lst[index]))
                queue.append(node.right)
                
            index += 1
            
        return root

# TC O(n)
# SC O(w)

class Codec:
    def serialize(self, root):
        self.res = []
        self.serialize_dfs_helper(root)
        return ",".join(self.res)
        
    def serialize_dfs_helper(self, node):
        if not node:
            self.res.append("None")
            return 
        
        self.res.append(str(node.val))
        self.serialize_dfs_helper(node.left)
        self.serialize_dfs_helper(node.right)

# TC O(n) # join / dfs
# SC O(n) # res

    def deserialize(self, data):
        self.lst = data.split(",")
        self.index = 0
        return self.deserialize_dfs_helper()
    
    def deserialize_dfs_helper(self):
        element = self.lst[self.index]
        self.index += 1
        
        if element == "None":
            return None
        
        node = TreeNode(int(element))
        node.left = self.deserialize_dfs_helper()
        node.right = self.deserialize_dfs_helper()
        
        return node

# TC O(n) # split / dfs
# SC O(n) # lst
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))