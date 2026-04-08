class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.right, self.left = Node(0,0), Node(0,0)
        self.right.prev, self.left.next = self.left, self.right
        

    def get(self, key: int) -> int:
        if key in self.cache:
            #place as mru
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            #return value
            return self.cache[key].val
        #default -1
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
    
    def insert(self, node):
        l, r = self.right.prev, self.right
        l.next, r.prev = node, node
        node.prev, node.next = l, r

    
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

            
        
        
