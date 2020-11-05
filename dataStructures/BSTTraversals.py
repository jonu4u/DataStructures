from dataStructures import BinarySearchTree
from dataStructures import QueueDs
from collections import deque
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

<<<<<<< Updated upstream
    list1=[]
    def in_order_dfs(self, node):
=======

    def in_order_dfs(self, node,list1):
>>>>>>> Stashed changes
         if node==None: return
         self.in_order_dfs(node.left,list1)
         # print(node.data)
         list1.append(node.data)
         self.in_order_dfs(node.right,list1)
         return list1

    def post_order(self,node):
        if node==None: return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)


    def level_order_bfs(self, root):
        # Take a q
        q=QueueDs.Queue()
        # put the root in the q
        q.enqueue(root)
        # peek returns first element from q.So till q is not null
        while q.peek() is not None:
            element_peeked=q.peek()
            print(element_peeked.dataVal.data)
            # left=left of element peeked and right is right
            left=element_peeked.dataVal.left
            right=element_peeked.dataVal.right
            # remove the peeked element
            q.dequeue()
            # if not none then put in q and loop
            if left is not None:
                q.enqueue(left)
            if right is not None:
                q.enqueue(right)

    def level_order_bfs_using_python_deque(self, root):
        # Take a q
        q=deque([root])
        # peek returns first element from q.So till q is not null
        while len(q)>0 and q[0] is not None:
            element_peeked=q.popleft()
            print(element_peeked.dataVal.data)
            # left=left of element peeked and right is right
            left=element_peeked.dataVal.left
            right=element_peeked.dataVal.right

            # if not none then put in q and loop
            if left is not None:
                q.append(left)
            if right is not None:
                q.append(right)



    # Useful Code to find height of the tree
    def height_tree(self, root):
        if root is None:
            return 0
        return max(self.height_tree(root.left), self.height_tree(root.right)) + 1

    # Useful Code to find node level in the tree
    def height_of_node(self,root, data) :
        return self.__getHeight__(root, data, 1)

    def __getHeight__(self,root, node, level):
        if (root == None):
            return 0

        if (root == node) :
            return level

        downlevel = self.__getHeight__(root.left,
                                       node, level + 1)
        if (downlevel != 0) :
            return downlevel

        downlevel = self.__getHeight__(root.right,
                                       node, level + 1)
        return downlevel

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
print(dfs.height_tree(t.tree))
print("Inorder-->",dfs.in_order_dfs(t.tree,[]))
print("BFS(Level Order)-->",dfs.level_order_bfs(t.tree))
