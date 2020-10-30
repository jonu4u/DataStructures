class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=1

class AVLTree:
    def __init__(self):
        self.root=None

    def height(self,root):
        # not root meaning root is None
        if not root:
            return 0
        return root.height


    def balance_factor(self,root):
        if not root:
            return 0
        return self.height(root.right)-self.height(root.left)

    # In left rotate we take right child for rotation
    def left_rotate(self,node):
        right=node.right
        # Take left child of right node and assign it to right of parent node
        temp = right.left
        node.right=temp
        right.left = node
        node.height = 1 + max(self.height(node.left),self.height(node.right))
        right.height=1 + max(self.height(right.left),self.height(right.right))
        return right

    # In right rotate we take left child for rotation
    def right_rotate(self,node):
        left =node.left
        temp = left.right
        node.left=temp
        left.right=node
        node.height = 1 + max(self.height(node.left),self.height(node.right))
        left.height=1 + max(self.height(left.left),self.height(left.right))
        return left

    def insert(self,value):
        self.root=self.__insert__(self.root,value)

    def __insert__(self,root,value):
        if not root:
            return Node(value)

        if value < root.value:
            root.left=self.__insert__(root.left,value)
        else:
            root.right=self.__insert__(root.right,value)

        root.height=1+max(self.height(root.left),self.height(root.right))

        balance=self.balance_factor(root)

        # This means tree is left heavy
        if balance<-1:
            # this means tree is fully left skewed
            if value<root.left.value:
                return self.right_rotate(root)
            # this means tree is left right skewed  so we need left rotation of left child and then right rotation of parent
            else:
                root.left=self.left_rotate(root.left)
                return self.right_rotate(root)

        # This means tree is right heavy
        if balance>1:
            # this means tree is fully right skewed
            if value>root.right.value:
                return self.left_rotate(root)
            # this means tree is right left skewed  so we need right rotation of right child and then left rotation of parent
            else:
                root.right=self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    # This is also called inorder predecessor
    def findLargestInLeftSubtee(self,root):
        currentValue = root.left
        while currentValue.right is not None:
            currentValue=currentValue.right
        return currentValue


    def delete(self,value):
        self.root=self.__delete__(self.root,value)

    def __delete__(self,root,value):
        if not root:
            return root
        elif value<root.value:
            root.left=self.__delete__(root.left,value)
        elif value>root.value:
            root.right=self.__delete__(root.right,value)
        else:
            if not root.left:
                temp=root.right
                root=None
                return temp
            elif not root.right:
                temp=root.left
                root=None
                return temp
            else:
               temp = self.findLargestInLeftSubtee(root)
               root.value=temp.value
               root.left=self.__delete__(root.left,temp.value)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left),self.height(root.right))
        bf=self.balance_factor(root)

        if bf<-1:
            # this means tree is fully left skewed
            if root.left.left is not None:
                return self.right_rotate(root)
            # this means tree is left right skewed  so we need left rotation of left child and then right rotation of parent
            else:
                root.left=self.left_rotate(root.left)
                return self.right_rotate(root)

        # This means tree is right heavy
        if bf>1:
            # this means tree is fully right skewed
            if root.right.right is not None:
                return self.left_rotate(root)
            # this means tree is right left skewed  so we need right rotation of right child and then left rotation of parent
            else:
                root.right=self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def printTree(self,root):
        print("Root Node",root.value)
        if root.left is None and root.right is None:
            print("Leaf Node",root.value)
            return
        if root.left is not None:
            print("Left parent is ",root.left.value)
            self.printTree(root.left)
        if root.right is not None:
            print("Right parent is ",root.right.value)
            self.printTree(root.right)




avl=AVLTree()
avl.insert(33)
avl.insert(13)
avl.insert(53)
avl.insert(61)
avl.insert(21)
avl.insert(11)
avl.insert(8)
avl.insert(9)
avl.printTree(avl.root)

# test the delete algo
print("---------")
avl.delete(13)
avl.printTree(avl.root)

print("---------")
avl.delete(33)
avl.printTree(avl.root)