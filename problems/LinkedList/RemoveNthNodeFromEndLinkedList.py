# 19. Remove Nth Node From End of List
#
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Follow up: Could you do this in one pass?
#
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]

# This is easy to don in 2 pass

# Let's try in ONE PASS

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd_using_hashmap(self, head, n):
        current=head
        index=0
        pointer_map={}
        while current is not None:
            pointer_map[index]=current
            index+=1
            current=current.next
        previous_node_index=index-n-1
        # it means the nth node doesn't exist, just return the head
        if previous_node_index<-1:
            return head
        # It means the nth node is the head itself
        elif previous_node_index==-1:
            head=head.next
            return head
        else:
            previous_n_node=pointer_map.get(index-n-1)
            previous_n_node.next=previous_n_node.next.next
            return head

s=Solution()
l1=ListNode(1)
l1.next=ListNode(2)
# l1.next.next=ListNode(3)
# l1.next.next.next=ListNode(4)
s.removeNthFromEnd_using_hashmap(l1,2)