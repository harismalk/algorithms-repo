# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0

        curr = head

        while curr:
            curr = curr.next
            
        length = count - n - 1

        l, r = head, head.next
        
        count = 0
        while l:
            if count == length:
                l.next = r.next
                break
            else:
                count +=1
            
        
        
        



        

        
        

    

        