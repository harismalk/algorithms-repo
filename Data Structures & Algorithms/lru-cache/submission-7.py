class Node:
    #initialize Node object
    def __init__(self, key, val):
        self.key = key
        self.val = val
class LRUCache:
    def __init__(self, capacity: int):
        #initialize cache
        self.cache = {}
        self.cap = capacity
        # self.right.prev will represent the most recently accessed
        self.right = Node(0,0)
        # self.left.next will represent the least recently accessed
        self.left = Node(0,0)

        #initialize the head + tail and our linkedin list 
        #(singly) to be connected

        self.right.prev = self.left
        self.left.next = self.right
    
    def insert(self, node):
        nxt, prv = self.right, self.right.prev
        prv.next = nxt.prev = node
        node.next, node.prev = nxt, prv
    
    def remove(self, node):
        nxt, prv = node.next, node.prev
        nxt.prev, prv.next = prv, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
