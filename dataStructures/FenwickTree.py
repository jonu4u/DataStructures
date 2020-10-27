class FenwickTree:
    def __init__(self,values=[]):
        # We need to make the fenwick Tree 1 based so we have to fill the initial slot with a default value and copy all elents from the input array
        # to the tree array starting from index 1.
        self.tree=[0]
        for i in range(0,len(values)):
            self.tree.append(values[i])

    def lsb(self,value):
        return value & -value

    def construct(self):
        tree = self.tree
        for i in range(1,len(tree)):
            parentIndex=self.getParentIndex(i)
            if parentIndex<len(tree) and parentIndex>0:
              tree[parentIndex] = tree[parentIndex] + tree[i]

    def getParentIndex(self,index):
        parentIndex= index+self.lsb(index)
        if parentIndex<len(self.tree):
            return parentIndex
        # If the parent is out of bounds we don't add anything. we return 0 as 0th index of array has 0 value as default.
        return 0


    def range_sum(self,i,j):
        if i>j:
            i,j=j,i
        return self.prefix_sum(j)-self.prefix_sum(i-1)

    def prefix_sum(self,index):
        sum=0
        while index>0:
            sum+=self.tree[index]
            index-=self.lsb(index)
        return sum

    def point_update(self,index,value):
        parentIndex=self.getParentIndex(index)
        if parentIndex<len(self.tree) and parentIndex>0:
            self.tree[index]=self.tree[index]+value
            self.point_update(parentIndex,value)
        else:
            self.tree[index]=self.tree[index]+value



fen=FenwickTree([2,5,8,12,4,6,3,7])
fen.construct()
print(fen.tree)

print(fen.range_sum(3,5))