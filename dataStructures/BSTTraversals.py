from dataStructures import BinarySearchTree
from dataStructures import QueueDs
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

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


    def level_order_bfs(self, root):
        height=self.height(root)
        for i in range(1,height+1):
            self.print_level(i)

    def height(self,node):
        if node is None:
            return 0;
        return max(self.height(node.left), self.height(node.right)) + 1

    def print_level(self,lvl):
        return








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
print(dfs.height(t.tree))
# print("Inorder-->",dfs.in_order_dfs(t.tree))
# print("BFS-->",dfs.level_order_bfs(t.tree).printQ())
