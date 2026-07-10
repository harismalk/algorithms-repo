class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = Node(0, None), Node(0, None)
        self.left.next, self.right.prev = self.right, self.left
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def insert(self, node):
        l, r = self.right.prev, self.right
        node.prev, node.next = l, r
        l.next, r.prev = node, node
    
    def remove(self, node):
        l, r = node.prev, node.next
        l.next, r.prev = r, l
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        
