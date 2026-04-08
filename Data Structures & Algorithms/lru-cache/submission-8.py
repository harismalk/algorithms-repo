class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(1,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def remove(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

    def insert(self, node):
        left, right = self.right.prev, self.right
        left.next = node
        right.prev = node

        node.next = right
        node.prev = left


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
