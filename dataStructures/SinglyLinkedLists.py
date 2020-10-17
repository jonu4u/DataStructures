class Node:
    def __init__(self,dataVal=None):
        self.dataVal=dataVal
        self.nextVal=None

class SinglyLinkedList:
    def __init__(self):
        self.headVal =None

    def listPrint(self):
        printVal = self.headVal
        while printVal is not None:
            print(printVal.dataVal)
            printVal = printVal.nextVal

    def insert(self,newElem,existingElem):
        newNode = Node(newElem)
        currentVal = self.headVal
        while currentVal.dataVal != existingElem:
            currentVal = currentVal.nextVal
        temp = currentVal.nextVal
        currentVal.nextVal=newNode
        newNode.nextVal=temp

    def remove(self,removeVal):
        if(removeVal==None or self.headVal ==None):
            return
        currentVal = self.headVal
        if(currentVal.dataVal == removeVal):
            self.headVal = currentVal.nextVal
            return
        while currentVal.nextVal.dataVal != removeVal:
            currentVal=currentVal.nextVal
        currentVal.nextVal = currentVal.nextVal.nextVal

    def removeLast(self):
        if(self.headVal is None or self.headVal.nextVal is None):
            self.headVal=None
            return
        currentVal = self.headVal
        while(currentVal.nextVal.nextVal is not None):
            currentVal=currentVal.nextVal
        currentVal.nextVal =None

    def addLast(self,elem):
        newNode = Node(elem)
        if(self.headVal is None):
            self.headVal = newNode
            return
        currentVal = self.headVal
        while currentVal.nextVal is not None:
            currentVal=currentVal.nextVal
        currentVal.nextVal=newNode

    def removeFirst(self):
        if(self.headVal is None or self.headVal.nextVal is None):
            self.headVal=None
            return
        self.headVal=self.headVal.nextVal

    def __len__(self):
        index=0
        currentVal=self.headVal
        while currentVal is not None:
            index=index+1
            currentVal=currentVal.nextVal
        return index

    def getElementAt(self,index):
        if(self.headVal is None or index>=len(self) or index<0):
            return None
        currentVal = self.headVal
        startIndex =0
        while startIndex!=index:
            currentVal=currentVal.nextVal
            startIndex=startIndex + 1
        return currentVal



# Tests
# list1 = SinglyLinkedList()
# list1.remove(30)
# list1.headVal = Node(10)
# elem2=Node(20)
# elem3=Node(30)
# list1.headVal.nextVal = elem2
# elem2.nextVal=elem3
# list1.listPrint()
# list1.removeFirst()
# list1.insert(90,30)
#
# list1.listPrint()
# list1.remove(None)
# print("below this line")
# list1.removeLast()
# list1.removeLast()
# list1.removeLast()
# list1.removeLast()
# list1.removeLast()
# list1.addLast(56)
# list1.addLast(50)
# list1.listPrint()

