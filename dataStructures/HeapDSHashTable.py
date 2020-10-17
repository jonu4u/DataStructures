from dataStructures.HashTableDs import HashTable
from dataStructures.HeapDs import Heap

class HeapHash:
    def __init__(self,items=[]):
        self.heap = items
        self.map = HashTable()
        self.mapAddAll(items)
        self.heapify(HeapHash.heapifyMinSubTree)

    def mapAdd(self,value,index):
        valueSet = self.map.get(value)
        if(valueSet is None):
            valueSet = [index]
            self.map.put(value,valueSet)
        else:
            valueSet.append(index)

    def mapAddAll(self,items):
        for index,item in enumerate(items):
            self.mapAdd(item,index)

    def insert(self,elem,func):
        self.heap.append(elem)
        self.mapAdd(elem,len(self.heap)-1)
        self.heapify(func)

    def mapRemove(self,value,index):
        valueSet = self.map.get(value)
        if(valueSet is None):
            return
        valueSet.remove(index)
        if len(valueSet)==0:
            self.map.remove(value)
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

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

    def fastRemove(self,elem,func):
        size =len(self.heap)
        indexOfElem = self.map.get(elem)[0]
        self.mapRemove(elem,indexOfElem)
        self.heap[indexOfElem]=self.heap[size-1]
        self.heap.pop(size-1)
        self.heapify(func)

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



# Test: here also passed function in Python inside a class in heapify
heap = HeapHash([9,8,7,6,5,4])
heap.heapify(HeapHash.heapifyMaxSubTree)
heap.printHeap()
heap.insert(1,HeapHash.heapifyMinSubTree)
heap.printHeap()
heap.insert(10,HeapHash.heapifyMaxSubTree)
heap.printHeap()
heap.insert(3,HeapHash.heapifyMinSubTree)
heap.printHeap()

#This below test is as per video of DS
heap1 = HeapHash([1,5,1,8,6,2,2,13,12,11,7,2,15,3,10])
heap1.printHeap()
print("popped ",heap1.pop(Heap.heapifyMinSubTree))
heap1.printHeap()
heap1.fastRemove(12,Heap.heapifyMinSubTree)
print("below    ")
heap1.printHeap()
heap1.fastRemove(3,Heap.heapifyMinSubTree)
print("below    ")
heap1.printHeap()
print("popped ",heap1.pop(Heap.heapifyMinSubTree))
heap1.printHeap()
heap1.fastRemove(6,Heap.heapifyMinSubTree)
print("below    ")
heap1.printHeap()