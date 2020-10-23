from dataStructures import BinarySearchTree
from dataStructures import QueueDs
class Traversals:
    def __init__(self):
        self.bfsq = QueueDs.Queue()

    def pre_order_dfs(self, node):
         if node==None: return
         print(node.data)
         self.pre_order_dfs(node.left)
         self.pre_order_dfs(node.right)


    def in_order_dfs(self, node):
         if node==None: return
         self.in_order_dfs(node.left)
         print(node.data)
         self.in_order_dfs(node.right)

    def post_order(self,node):
        if node==None: return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)


    def level_order_bfs(self, node, rightNode=None):
         if node==None:return
         left = node.left
         right = node.right
         self.bfsq.enqueue(node.data)
         if rightNode:
             self.bfsq.enqueue(rightNode.data)
         if left is None and right is None:
             return self.bfsq
         if left and right:
             self.level_order_bfs(left, right)
             return self.bfsq
         if left and right is None:
             self.level_order_bfs(left, right)
             return self.bfsq
         else:
             self.level_order_bfs(right, left)
             return self.bfsq



t = BinarySearchTree.BST()
t.insertNode(7)
t.insertNode(5)
t.insertNode(4)
t.insertNode(6)
t.insertNode(20)
t.insertNode(8)
t.insertNode(11)
t.insertNode(15)
t.insertNode(10)

dfs = Traversals()
print("Inorder-->",dfs.in_order_dfs(t.tree))
print("BFS-->",dfs.level_order_bfs(t.tree).printQ())
