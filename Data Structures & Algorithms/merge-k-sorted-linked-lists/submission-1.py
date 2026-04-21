# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        minHeap = []
        uuid = 0

        for l in lists:
            if l:
                heapq.heappush(minHeap, [l.val, uuid, l])
                uuid+=1
                
        
        while minHeap:
            val, _, ptr = heapq.heappop(minHeap)
            newNode = ListNode(val)
            curr.next = newNode
            curr = curr.next
            if ptr.next:
                ptr = ptr.next
                heapq.heappush(minHeap, [ptr.val, uuid, ptr])
                uuid+=1
        
        return dummy.next
             

            

            


        