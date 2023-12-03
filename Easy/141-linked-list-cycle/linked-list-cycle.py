# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        pointers = set()
        
        if not head:
            return False
        
        while cur.next:
            pointers.add(id(cur))
            cur = cur.next

            if id(cur) in pointers:
                return True
        return False
        