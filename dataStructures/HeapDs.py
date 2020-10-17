class Heap:
    def __init__(self,items=[]):
        self.heap = items
        self.heapify(Heap.heapifyMinSubTree)

    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def heapifyMinSubTree(self,index):
        size = len(self.heap)
        largest = index
        leftNode = 2*index+1
        rightNode = 2*index+2
        if(leftNode<size and self.heap[leftNode]<self.heap[index]):
            largest = leftNode
        if(rightNode<size and self.heap[largest]>self.heap[rightNode]):
            largest= rightNode
        if largest!=index:
            self.swap(largest,index)
            self.heapifyMinSubTree(largest)

    def printHeap(self):
         for i in range(0,len(self.heap),1):
             print(self.heap[i])

    def insert(self,elem,func):
        self.heap.append(elem)
        self.heapify(func)

    def heapifyMaxSubTree(self,index):
        size=len(self.heap)
        largest = index
        leftNode= 2*index+1
        rightNode= 2*index+2
        if(leftNode<size and self.heap[leftNode]>self.heap[index]):
            largest=leftNode
        if(rightNode<size and self.heap[largest]<self.heap[rightNode]):
            largest=rightNode
        if largest!=index:
            self.swap(largest,index)
            self.heapifyMaxSubTree(largest)

    def heapify(self,func):
        startingIndex = int((len(self.heap)//2) -1)
        for i in range(startingIndex,-1,-1):
            func(self,i)

    # Pop takes root elemnet from heap
    def pop(self,func):
        size =len(self.heap)
        if(size==0):
            return None
        if(size ==1):
            top = self.heap[0]
            self.heap.clear()
            return top
        top = self.heap[0]
        self.heap[0]=self.heap[size-1]
        self.heap.pop(size-1)
        self.heapify(func)
        return top

    def naiveRemove(self,elem,func):
        size =len(self.heap)
        indexOfElem = self.heap.index(elem)
        self.heap[indexOfElem]=self.heap[size-1]
        #del statement or pop can delete element from a list given it's index
        del self.heap[size-1]
        self.heapify(func)

    #Hashtable implementation
    def advancedRemove(self,elem):
        return



# Test: here also passed function in Python inside a class in heapify
# heap = Heap([9,8,7,6,5,4])
# heap.heapify(Heap.heapifyMaxSubTree)
# heap.printHeap()
# heap.insert(1,Heap.heapifyMinSubTree)
# heap.printHeap()
# heap.insert(10,Heap.heapifyMaxSubTree)
# heap.printHeap()
# heap.insert(3,Heap.heapifyMinSubTree)
# heap.printHeap()

# This below test is as per video of DS
# heap1 = Heap([1,5,1,8,6,2,2,13,12,11,7,2,15,3,10])
# heap1.printHeap()
# print("popped ",heap1.pop(Heap.heapifyMinSubTree))
# heap1.printHeap()
# heap1.naiveRemove(12,Heap.heapifyMinSubTree)
# print("below    ")
# heap1.printHeap()
# heap1.naiveRemove(3,Heap.heapifyMinSubTree)
# print("below    ")
# heap1.printHeap()
# print("popped ",heap1.pop(Heap.heapifyMinSubTree))
# heap1.printHeap()
# heap1.naiveRemove(6,Heap.heapifyMinSubTree)
# print("below    ")
# heap1.printHeap()