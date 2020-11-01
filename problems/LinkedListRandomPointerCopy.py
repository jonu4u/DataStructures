# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        node_position_map={}
        index=0
        current=head
        while current is not None:
            # In this map we see the position of each node as well as we create a new node only with value of old node
            node_position_map[current]=(index,Node(current.val))
            index+=1
            current=current.next
        new_list=None
        for key,value in node_position_map.items():
            # The new_list is the element when index=0
            if value[0]==0:
                new_list=value[1]
            # For each key we find the random and next node. We find that corresponding node from map and assign the newly created nodes
            # to the current value node which we're on
            random_node=key.random
            next_node=key.next
            if next_node is not None:
                value[1].next=node_position_map.get(next_node)[1]
            if random_node is not None:
                value[1].random=node_position_map.get(random_node)[1]

        return new_list

s=Solution()
head=Node(7,random=None)
node2=Node(13,random=head)
head.next=node2
node4=Node(10,random=node2)
node3=Node(11,random=node4)
node2.next=node3
node3.next=node4
node5=Node(1,random=head)
node4.next=node5


s.copyRandomList(head)




