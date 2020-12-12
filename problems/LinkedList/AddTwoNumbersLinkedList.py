# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
#
# Example 1:
# L1= 2->4->3(342)
# L2=5->6->4(465)
# Output = 807, 7->0->8
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# Definition for singly-linked list.
from dataStructures import SinglyLinkedLists
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers_naive(self, l1, l2):
        num1=self.get_number(l1)
        num2=self.get_number(l2)
        new_list=None
        return self.create_list_from_number(num2+num1,new_list)

    def create_list_from_number(self,number,head):
           head=ListNode(number%10)
           number=number//10
           current=head
           while number>0:
               digit=number%10
               current.next=ListNode(digit)
               number=number//10
               current=current.next
           return head

    def get_number(self,head):
        sum=0
        currentNode=head
        power=0
        while currentNode is not None:
            sum=sum+currentNode.val*(10**power)
            power+=1
            currentNode=currentNode.next
        return sum

s=Solution()
l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)
l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)

print(s.addTwoNumbers_naive(l1,l2))