class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.cap = capacity
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def insert(self, node):
        left, right = self.right.prev, self.right
        left.next, right.prev = node, node
        node.prev, node.next = left, right
    
    def remove(self, node):
        left, right = node.prev, node.next
        left.next, right.prev = right, left

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)
        if self.cap < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
