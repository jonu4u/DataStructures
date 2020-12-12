# 143. Reorder List
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
#
# Example 2:
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# This solution requires modification IN PLACE in the same list
class Solution(object):
    def reorderList(self, head):
        if head is None:
            return head
        index=0
        current=head
        position_map={}
        while current is not None:
            position_map[index]=current
            index+=1
            current=current.next
        first,last=0,index-1
        half=index//2
        while first<half:
              first_node=position_map.get(first)
              last_node=position_map.get(last)
              # It is important to make the penultimate node the last node else
              # it'll be a infinite loop
              position_map.get(last-1).next=None
              # for even nodes this is the case
              if first_node.next==last_node:
                  continue
              # Make the last nodes next as first nodes next, then make the first nodes next as last node
              last_node.next=first_node.next
              first_node.next=last_node
              # Move counter to left and right by one place
              first+=1
              last-=1

s=Solution()
l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)
l1.next.next.next=ListNode(4)
s.reorderList(l1)