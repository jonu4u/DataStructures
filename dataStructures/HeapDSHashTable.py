from dataStructures.HashTableDs import HashTable

# This class has heap backed by a hashtable, so that while searching them we get them in O(1)[best case] and O(n) worst case
# So remove methods take advantage of this and quickly remove element as it can find it quickly from hashtable instead of linear searching in last case.
class HeapHash:
    def __init__(self,items=[]):
        self.heap = items
        # This map keeps track of values in the heap and what indices they are present
        self.map = HashTable()
        self.mapAddAll(self.heap)
        self.heapify(HeapHash.heapifyMinSubTree)

    def mapAdd(self,value,index):
        # Since it is a hashtable key is the value(data value) and the value is list which
        # contains all the indices the key is present. So when I do get on map I get a list for a key.
        valueSet = self.map.get(value)
        if(valueSet is None):
            valueSet = [index]
            self.map.put(value,valueSet)
        else:
            valueSet.append(index)

    # This method swaps the index position when a value is swapped in the map.
    def mapSwap(self, valueList1, index1, valueList2, index2):
        valueList1.remove(index1)
        valueList2.remove(index2)
        valueList1.append(index2)
        valueList2.append(index1)

    def mapAddAll(self,items):
        for index,item in enumerate(items):
            self.mapAdd(item,index)

    def mapRemove(self,value,index):
        valueSet = self.map.get(value)
        if(valueSet is None):
            return
        valueSet.remove(index)
        if len(valueSet)==0:
            self.map.remove(value)

    def swap(self,i,j):
        # Remember map.get always returns a list.
        valueList1 = self.map.get(self.heap[i])
        valueList2 = self.map.get(self.heap[j])
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
        self.mapSwap(valueList1,i,valueList2,j)

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

    def insert(self,elem,func):
        self.heap.append(elem)
        self.mapAdd(elem,len(self.heap)-1)
        self.heapify(func)

    # Pop takes root element from heap
    def pop(self,func):
        size =len(self.heap)
        if(size==0):
            return None
        if(size ==1):
            top = self.heap[0]
            self.heap.clear()
            return top
        top = self.heap[0]
        self.mapRemove(top,0)
        self.mapRemove(self.heap[size-1],size-1)
        self.mapAdd(self.heap[size-1],0)
        self.heap[0]=self.heap[size-1]
        self.heap.pop(size-1)
        self.heapify(func)
        return top

    def fastRemove(self,elem,func):
        size =len(self.heap)
        indexOfElem = self.map.get(elem)[0]
        # When an element is removed from heap, the last element is assigned to the index of the removed position, so
        # our map needs to first remove both the last and the current element index and then add the new index of the current
        # element.
        self.mapRemove(elem,indexOfElem)
        self.mapRemove(self.heap[size-1],size-1)
        self.mapAdd(self.heap[size-1],indexOfElem)
        self.heap[indexOfElem]=self.heap[size-1]
        self.heap.pop(size-1)
        self.heapify(func)



# Test: here also passed function in Python inside a class in heapify
# heap = HeapHash([9,8,7,6,5,4])
# heap.heapify(HeapHash.heapifyMaxSubTree)
# heap.printHeap()
# heap.insert(1,HeapHash.heapifyMinSubTree)
# heap.printHeap()
# heap.insert(10,HeapHash.heapifyMaxSubTree)
# heap.printHeap()
# heap.insert(3,HeapHash.heapifyMinSubTree)
# heap.printHeap()
#
# #This below test is as per video of DS
# heap1 = HeapHash([1,5,1,8,6,2,2,13,12,11,7,2,15,3,10])
# heap1.printHeap()
# print("popped ",heap1.pop(Heap.heapifyMinSubTree))
# heap1.printHeap()
# heap1.fastRemove(12,Heap.heapifyMinSubTree)
# print("below    ")
# heap1.printHeap()
# heap1.fastRemove(3,Heap.heapifyMinSubTree)
# print("below    ")
# heap1.printHeap()
# print("popped ",heap1.pop(Heap.heapifyMinSubTree))
# heap1.printHeap()
# heap1.fastRemove(6,Heap.heapifyMinSubTree)
# print("below    ")
# heap1.printHeap()

#This below test is as per video of DS in HAshtable
# heap1 = HeapHash([2,7,2,11,7,13,2])
# heap1.printHeap()
# print(heap1.map.arr)
# heap1.insert(3,HeapHash.heapifyMinSubTree)
# heap1.printHeap()
# print(heap1.map.arr)
# heap1.fastRemove(2,HeapHash.heapifyMinSubTree)
# heap1.printHeap()
# print(heap1.map.arr)
# heap1.pop(HeapHash.heapifyMinSubTree)
# heap1.printHeap()
# print(heap1.map.arr)