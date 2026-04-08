# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        existed = set()

        while head:
            if head in existed:
                return True
            else:
                existed.add(head)
                head = head.next
        
        return False
        
