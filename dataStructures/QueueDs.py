from dataStructures import SinglyLinkedLists


class Queue:
    def __init__(self):
        self.queue = SinglyLinkedLists.SinglyLinkedList()
    # Adds element to q at the end since q is FIFO
    def enqueue(self,elem):
        self.queue.addLast(elem)

    # Removes 1st element
    def dequeue(self):
        self.queue.removeFirst()

    def printQ(self):
        self.queue.listPrint()

    # This returns the first element from q
    def peek(self):
        return self.queue.getElementAt(0)



#Test
# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.printQ()
# q.dequeue()
# q.printQ()
