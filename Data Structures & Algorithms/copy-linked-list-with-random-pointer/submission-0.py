"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       
        #Explicitly map None to None
        oldToCopy = {None: None}

        curr = head

        #create all new nodes, store them as values in hashmap
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        

        curr = head

        #go through old again, get corresponding new nodes and assign the pointers
        while curr:
           copy = oldToCopy[curr]
           copy.next = oldToCopy[curr.next]
           copy.random = oldToCopy[curr.random]
           curr = curr.next

        return oldToCopy[head]

         
        
         


         

        
        

        

        

        


        