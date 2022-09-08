# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        if head.next != None:
            if (head.val == head.next.val) & (head.next.next != None):
                head.next = head.next.next
                self.deleteDuplicates(head)
            elif (head.val == head.next.val) & (head.next.next == None):
                head.next = None
            else:
                self.deleteDuplicates(head.next)
        return head