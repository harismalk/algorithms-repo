# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s_n1 = ""
        s_n2 = ""

        cur1 = l1
        cur2 = l2

        while cur1:
            s_n1 += str(cur1.val)
            cur1 = cur1.next
        while cur2:
            s_n2 += str(cur2.val)
            cur2 = cur2.next
        
        s_n1 = s_n1[::-1]
        s_n2 = s_n2[::-1]

        int1 = int(s_n1)
        int2 = int(s_n2)

        int3 = int1 + int2

        s_n3 = (str(int3))[::-1]

        head = ListNode(int(s_n3[0]), None)
        l = head


        for i in range(1, len(s_n3)):
            l.next = ListNode(int((s_n3)[i]), None)
            l = l.next

        return head




        