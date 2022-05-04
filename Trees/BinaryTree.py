# ---------------------------------------------------------------------------------------------------------
# ------------------------------------------------BINARY-TREES---------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# Represent Hierarchical data
# Databases
# Autocompletion                                      5
# Compilers                                         /   \
# Compression                                      2     8
# left < node < right                             / \   / \
# Insert  O(1) .                                 1   3 6   9
# Lookpup O(1)
# Remove  O(1)
# Traversals
# Breath first:
# The binary tree is traversed in order ex. 5,2,8,1,3,6,9 is called level order traversal
# Depth first:
# 1. Pre-order  Root, left, right :  5,2,1,3,8,6,9
# 2. In-order   Left, root, right :  1,2,3,5,6,8,9    They are ordered
# 3. Post-order Left, right, root :  1,3,2,6,9,8,5
import sys
class BinaryTree:
    def __init__(self):
        self.root = None    

    class Node:
        def __init__(self, value):
            self.value = value
            self.leftNode = None
            self.rightNode = None

    def add(self,value):
        if value is None:
            raise ValueError("Empty value.")
        self.root = self._add_recursion(self.root,value)

    def _add_recursion(self,node,value):
        if node == None:
            node = self.Node(value)
        if value > node.value:
            node.rightNode = self._add_recursion(node.rightNode,value)
        elif value < node.value:
            node.leftNode = self._add_recursion(node.leftNode,value)
        return node

    def find(self,value):
        if value is None:
            raise ValueError("Empty value.")
        return self.find_recursion(self.root,value)

    def find_recursion(self,node,value):
        exist = False
        if node is None:
            return False
        if node.value == value:
            return True
        if value > node.value:
            exist = self.find_recursion(node.rightNode,value)
        elif value < node.value:
            exist = self.find_recursion(node.leftNode,value)
        return exist

    def BreathFirst(self):

        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.value)
            if current.leftNode != None:
                queue.append(current.leftNode)
            if current.rightNode != None:
                queue.append(current.rightNode)


    
    def PreOrderTraversal(self):
        self._DepthFirstPreOrderTraversal(self.root)

    def _DepthFirstPreOrderTraversal(self,root):
        #root (print)
        #left
        #right
        if root is None:
            return
        print(root.value)
        self._DepthFirstPreOrderTraversal(root.leftNode)
        self._DepthFirstPreOrderTraversal(root.rightNode)
    
    def InOrderTraversal(self):
        self._DepthFirstInOrderTraversal(self.root)

    def _DepthFirstInOrderTraversal(self,root):
        #left
        #root (print)
        #right
        if root is None:
            return
        self._DepthFirstInOrderTraversal(root.leftNode)
        print(root.value)
        self._DepthFirstInOrderTraversal(root.rightNode)

    def PostOrderTraversal(self):
        self._DepthFirstPostOrderTraversal(self.root)

    def _DepthFirstPostOrderTraversal(self,root):
        #left
        #right
        #root (print)
        if root is None:
            return
        self._DepthFirstPostOrderTraversal(root.leftNode)
        self._DepthFirstPostOrderTraversal(root.rightNode)
        print(root.value)

    def height(self):
        return self.height_tree(self.root)

    def height_tree(self,root):
        # Calculate the height of a Node 1 + max(height(L)+height(R))
        # Here we use post-order traversal - we go first to leaves
        if root is None:
            return -1
        if root.leftNode is None and root.rightNode is None:
            return 0
        return 1 + max(self.height_tree(root.leftNode), self.height_tree(root.rightNode))


    def minimum(self):
        return self.minimum_value_BST(self.root)

    def minimum_value_BST(self,root):
        if root is None:
            raise ValueError
        current = root
        while(current.leftNode != None):
            current= current.leftNode
        return current.value


    def equals(self,tree):
        return self.equals_tree(self, self.root, tree.root)

    def equals_tree(self,node, nodeother):
        #First root is validated and then the childs of that root are send recursively to the method, if everythings ok both of them must be null
        #otherwise the return false will be triggered
        if node == nodeother == None:
            return True
        if node is not None and nodeother is not None:
            return node.value == nodeother.value and self.equals_tree(node.leftNode, nodeother.leftNode) and self.equals_tree(node.rightNode,nodeother.rightNode)
        return False

    def validateBinarySearchTree(self):
        return self.validateBinarySearchTreeImpl(self.root, -sys.maxsize , sys.maxsize)

    def validateBinarySearchTreeImpl(self,root, min , max):
        if root is None:
            return True
        if root.value < min or root.value > max:
            return False
        return self.validateBinarySearchTreeImpl(root.leftNode,min,root.value -1) and self.validateBinarySearchTreeImpl(root.rightNode,root.value+1,max)


    def nodesAtKDistance(self,target):
        level = 0
        queue = []
        if self.root is None:
            return 
        queue.append(self.root)
        level +=1
        while queue:
            if level == target:
                return [x.value for x in queue]
            current = queue.pop()
            if current.leftNode is not None:
                queue.append(current.leftNode)
            if current.rightNode is not None:
                queue.append(current.rightNode)
            level +=1
        return -1

    def vertical_traversal(self):
        if self.root is None:
            return []
        #[x,y,root.val]
        coordinates = self.vertical_dfs(self.root,0,0,[])
        coordinates.sort(key=lambda x: (x[0],-x[1],x[2]))
        result = [[coordinates[0][2]]]
        for i in range(1,len(coordinates)):
            if coordinates[i][0] == coordinates[i-1][0]:
                result[-1].append(coordinates[i][2])
            else:
                result.append([coordinates[i][2]])
        return result
    def vertical_dfs(self,node,x,y,coordinates):
        if not node:
            return coordinates
        coordinates.append([x,y,node.value])
        self.vertical_dfs(node.leftNode,x-1,y-1,coordinates)
        self.vertical_dfs(node.rightNode,x+1,y-1,coordinates)
        return coordinates

    def min_prev_target(self,target):
        return self.in_order_min_prev_target(self.root,target)

    #O(h) where h is heoght of tree
    def in_order_min_prev_target(self,node,target):
        if node is None:
            return -1
        if node.value == target:
            return target
        elif node.value < target:
            k = self.in_order_min_prev_target(node.rightNode,target)
            if k == -1:
                return node.value
            else:
                return k
        elif node.value > target:
            return self.in_order_min_prev_target(node.leftNode,target)
    def diameter_tree(self):
        return self.diameter_tree_r(self.root)
    def diameter_tree_r(self,root):
        self.max_diameter = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right= dfs(node.right)
            self.max_diameter = max(left+right,self.max_diameter)
            return 1 + max(left,right)
        dfs(root)
        return self.max_diameter



# Autocompletion                                      5
# Compilers                                         /   \
# Compression                                      2     8
# left < node < right                             / \   / \
# Insert  O(1) .                                 1   3 6   9
#                                                           \
#                                                           25

    
z = BinaryTree()
s = [5,2,8,1,3,6,9,25]
for item in s:
    z.add(item)

print(z.diameter_tree())
        
        
