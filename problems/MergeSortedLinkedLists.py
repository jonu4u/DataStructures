# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example 1:
#
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return l1
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        new_list=None
        current1=l1
        current2=l2
        if current1.val>current2.val:
            new_list=current2
            current2=current2.next
        else:
            new_list=current1
            current1=current1.next

        current=new_list
        while current1 is not None:
            # edge case 1: One element in each list, so current2 also needs to be checked
            if current2 is not None and current1.val>current2.val:
                current.next=current2
                current2=current2.next
            else:
                current.next=current1
                current1=current1.next
            current=current.next
        # edge case 2: when last element is same of both lists we exhaust list1 but something in list 2 still remains,
        # so whatever is left in list2 we append to end of currentlist
        if current2 is not None:
            current.next=current2
        return new_list