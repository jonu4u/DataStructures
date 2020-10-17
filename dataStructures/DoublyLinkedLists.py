class Node:
    def __init__(self,dataVal=None):
        self.nextVal =None
        self.prevVal =None
        self.dataVal=dataVal

class DLinkedList:
    def __init__(self):
        self.headVal=None

    def listPrint(self):
        printVal =self.headVal
        while printVal is not None:
            print(printVal.dataVal)
            printVal=printVal.nextVal

    def push(self,value):
        newValue = Node(value)
        newValue.nextVal = self.headVal
        if(self.headVal is not None):
            self.headVal.prevVal= newValue
        self.headVal = newValue

    def addBefore(self,beforeValue,newValue):
        newNode = Node(newValue)
        valueNode = self.headVal
        while valueNode.dataVal != beforeValue:
            valueNode=valueNode.nextVal
        prevNode = valueNode.prevVal
        if(prevNode is None):
            self.headVal = newNode
        else:
            prevNode.nextVal=newNode
            newNode.prevVal = prevNode
        newNode.nextVal = valueNode
        valueNode.prevVal = newNode

    def remove(self,removeValue):
        valueNode = self.headVal
        while valueNode.dataVal != removeValue:
            valueNode=valueNode.nextVal
        prevNode = valueNode.prevVal
        nextNode = valueNode.nextVal
        if(prevNode is None):
            self.headVal = nextNode
            self.headVal.prevVal = None
            return
        if(nextNode is None):
            prevNode.nextVal = nextNode
            return
        prevNode.nextVal = nextNode
        nextNode.prevVal = prevNode

    def addAfter(self,afterValue,newvalue):
        newNode = Node(newvalue)
        aftervalueNode = self.headVal
        while aftervalueNode.dataVal!=afterValue:
            aftervalueNode=aftervalueNode.nextVal
        nextNode = aftervalueNode.nextVal
        if(nextNode is None):
            aftervalueNode.nextVal = newNode
            newNode.prevVal=aftervalueNode
            return
        aftervalueNode.nextVal = newNode
        newNode.prevVal = aftervalueNode
        newNode.nextVal=nextNode
        nextNode.prevVal=newNode

    def length(self):
        size = 0
        currentVal = self.headVal
        while(currentVal is not None):
            size =size +1
            currentVal=currentVal.nextVal
        return size

    def getIndexOfElem(self,elemValue):
        index =0
        currentNode = self.headVal
        while (currentNode is not None and currentNode.dataVal != elemValue) :
            index=index +1
            currentNode=currentNode.nextVal
        if(currentNode is None):
            return -1
        return index


#Tests
# list = DLinkedList()
# list.push(10)
# print("Index is  ",list.getIndexOfElem(10))
# list.addAfter(10,30)
# list.addAfter(10,40)
# list.addAfter(30,40)
# list.addAfter(40,50)
# list.push(20)
# list.push(80)
# list.addBefore(10,90)
# list.addBefore(80,100)
# list.remove(40)
# list.addBefore(40,200)
# list.remove(50)
# list.remove(10)
# list.listPrint()
# print("Index is  ",list.getIndexOfElem(200))
# print("Index is  ",list.length())

