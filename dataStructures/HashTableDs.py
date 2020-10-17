class HashTable:
    def __init__(self,size=10):
        self.size=size
        #This creates size number of lists inside a list. So a 2D list kindof.
        self.arr=[[] for i in range(self.size)]
        # print(self.arr)

    def getHash(self,key):
        return hash(key)%self.size

    def put(self,key,value):
        hashKey = self.getHash(key)
        # This is a list
        isKeyExists=False
        currentElem = self.arr[hashKey]
        for index,elem in enumerate(currentElem):
            if (elem[0]==key):
                list1 = list(elem)
                list1[1]=value
                currentElem[index]=tuple(list1)
                isKeyExists=True
                break
        if not isKeyExists:
            currentElem.append((key,value))

    def get(self,key):
        hashKey=self.getHash(key)
        bucket = self.arr[hashKey]
        if bucket is None:
            return
        for elem in bucket:
            if(elem[0]==key):
                return elem[1]
        return

h= HashTable()
h.put("20",10)
h.put("20",20)
h.put("10",10)
h.put("30",30)
h.put("40",40)
h.put("50",50)
h.put("60",60)
h.put("70",70)
h.put("80",10)
h.put("90",90)
h.put("120",120)
h.put("200",200)
h.put("1000",10000)
h.put("12783448u83u",50)
h.put("21",21)
print(h.get("1000"))