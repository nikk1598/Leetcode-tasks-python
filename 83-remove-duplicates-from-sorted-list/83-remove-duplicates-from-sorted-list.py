# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        cur = head
        while cur.next != None:
            if (cur.val == cur.next.val) & (cur.next.next != None):
                cur.next = cur.next.next
            elif (cur.val == cur.next.val) & (cur.next.next == None):
                cur.next = None
            else:
                cur = cur.next
                
        return head
                