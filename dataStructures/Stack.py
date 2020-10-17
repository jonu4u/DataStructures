from dataStructures import SinglyLinkedLists


class Stack:
    def __init__(self):
        self.stack = SinglyLinkedLists.SinglyLinkedList()

    def push(self,element):
        self.stack.addLast(element)

    def pop(self):
        size = len(self.stack)
        current = self.stack.getElementAt(size-1)
        if(current is None):
            return None
        self.stack.removeLast()
        return current.dataVal

    def printStack(self):
        self.stack.listPrint()

# Test
# stack1 = Stack()
# stack1.push(5)
# stack1.push(6)
# stack1.printStack()
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())
# stack1.printStack()
