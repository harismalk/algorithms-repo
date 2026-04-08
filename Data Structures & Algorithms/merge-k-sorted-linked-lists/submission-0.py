# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode(0,None)
        res = dummy
        minHeap = []

        for i, head in enumerate(lists):
            heapq.heappush(minHeap, [head.val, i, head])
        
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            dummy.next = node
            dummy = dummy.next
            node = node.next
            if node:
                heapq.heappush(minHeap, [node.val, i, node])
        
        return res.next



