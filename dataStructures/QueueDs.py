from dataStructures import SinglyLinkedLists


class Queue:
    def __init__(self):
        self.queue = SinglyLinkedLists.SinglyLinkedList()

    def enqueue(self,elem):
        self.queue.addLast(elem)

    def dequeue(self):
        self.queue.removeFirst()

    def printQ(self):
        self.queue.listPrint()

#Test
# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.printQ()
# q.dequeue()
# q.printQ()
