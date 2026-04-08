class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        

    def insert(self, node):
        nxt, prv = self.right, self.right.prev
        node.next, node.prev = nxt, prv
        nxt.prev = prv.next = node

    def remove(self, node):
        nxt, prv = node.next, node.prev
        prv.next, nxt.prev = nxt, prv

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

        
