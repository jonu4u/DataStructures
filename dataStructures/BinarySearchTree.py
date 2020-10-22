class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

class BST:
    def __init__(self):
        # Initially the Tree is null
        self.tree = None
        self.counter = 0

    def insertNode(self,value):
        newNode=Node(value)
        if self.tree is None:
            self.tree = newNode
            return
        parent_insert_node=self.find_parent_insertion_node(self.tree, value)
        if value > parent_insert_node.data:
            parent_insert_node.right=newNode
        else:
            parent_insert_node.left=newNode

    def find_parent_insertion_node(self,rootNode,value):
        leftNode = rootNode.left
        rightNode = rootNode.right
        if value > rootNode.data:
            if rightNode is None:
                return rootNode
            rootNode=rightNode
        else:
            if leftNode is None:
                return rootNode
            rootNode=leftNode
        return self.find_parent_insertion_node(rootNode,value)

    def find_parent_child_non_root_node(self,rootNode,value):
        left = rootNode.left
        right = rootNode.right

        if value>rootNode.data:
            currentNode=right
        else:
            currentNode=left
        if currentNode is not None:
            if currentNode.data==value:
                return (rootNode,currentNode)
            else:
                return self.find_parent_child_non_root_node(currentNode,value)
        else:
            #Case when element doesn't exist in tree
            return (None,None)


    def printTree(self,root):
        print("Root Node",root.data)
        if root.left is None and root.right is None:
            print("Leaf Node",root.data)
            return
        if root.left is not None:
            print("Left parent is ",root.left.data)
            self.printTree(root.left)
        if root.right is not None:
            print("Right parent is ",root.right.data)
            self.printTree(root.right)

    def findLargestInLeftSubtee(self,head):
        currentValue = head.left
        while currentValue.right is not None:
            currentValue=currentValue.right
        return currentValue

    def remove(self,value):
        rootNode= self.tree
        # Tree is empty
        if rootNode is None:
            return

        #Delete the rootNode
        if rootNode.data == value:
            #Case 1: If only one node is present
            if rootNode.left is None and rootNode.right is None:
                rootNode=None
                return
            #Case 2: If root node has either left child or right child
            if rootNode.left is None and rootNode.right is not None:
                rootNode=rootNode.right
                return
            if rootNode.left is not None and rootNode.right is None:
                rootNode=rootNode.left
                return

            #Case 3: If rootNode has both Child
            replacedValue = self.findLargestInLeftSubtee(rootNode)
            self.remove(replacedValue.data)
            rootNode.data=replacedValue.data
            return

        #Write code for non root
        parentNodeValue,currentValueNode=self.find_parent_child_non_root_node(rootNode,value)
        #If value is not in Tree
        if currentValueNode is None:
            return
        if self.counter==0:
            actualValue=currentValueNode
        self.counter+=1
        is_current_value_left_child = True if parentNodeValue.left ==currentValueNode else False
        #Case 1: When value to be deleted is leaf node
        if currentValueNode.left is None and currentValueNode.right is None:
            if is_current_value_left_child:
                parentNodeValue.left=None
            else:
                parentNodeValue.right=None
            currentValueNode=None#this step is to free up but optional in python
            return

        #Case 2: When value to be deleted has either left or right child
        if currentValueNode.left is not None and currentValueNode.right is None:
            if is_current_value_left_child:
                parentNodeValue.left=currentValueNode.left
            else:
                parentNodeValue.right=currentValueNode.left
            currentValueNode=None
            return
        if currentValueNode.left is None and currentValueNode.right is not None:
            if is_current_value_left_child:
                parentNodeValue.left=currentValueNode.right
            else:
                parentNodeValue.right=currentValueNode.right
            currentValueNode=None
            return

        #Case 3: When the node to be removed has both left and right child

        #Find the largest left Subtree and this will surely be case 1 or case 2
        replacedValue = self.findLargestInLeftSubtee(currentValueNode)
        self.remove(replacedValue.data)
        actualValue.data=replacedValue.data
        return


# # This tree also handles duplicate values in the tree by removing the 1st one.
# bst = BST()
# bst.insertNode(7)
# bst.insertNode(20)
# bst.insertNode(5)
# bst.insertNode(15)
# bst.insertNode(10)
# bst.insertNode(4)
# bst.insertNode(4)
# bst.insertNode(33)
# bst.insertNode(2)
# bst.insertNode(25)
# bst.insertNode(6)
# bst.remove(3455)
# bst.printTree(bst.tree)
# print("Below  ---")
# bst.remove(4)
# bst.printTree(bst.tree)
# print("Below  ---")
# bst.remove(20)
# bst.printTree(bst.tree)
# print("Below  ---")
# bst.remove(7)
# bst.printTree(bst.tree)





