class LRUCache:
    class Node:
        def __init__(self,val,key=-1):
            self.nextnode = None
            self.prev = None
            self.val = val
            self.key = key

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(0)
        self.tail = self.Node(0)
        self.head.nextnode = self.tail
        self.tail.prev = self.head
        self.hashmap = {}

    def add_after_head(self,node):
        buf = self.head.nextnode
        buf.prev = node
        self.head.nextnode = node
        node.nextnode = buf
        node.prev = self.head

    def move_to_front(self,node):
        prev = node.prev
        nex = node.nextnode
        prev.nextnode = nex
        nex.prev = prev
        self.add_after_head(node)



    def evict(self):
        
        prev = self.tail.prev.prev
        node = prev.nextnode
        prev.nextnode = self.tail
        self.tail.prev = prev
        self.hashmap.pop(node.key,None)

    def get(self, key: int) -> int:
        # check the map
        if not self.hashmap.get(key):
            return -1
        node = self.hashmap.get(key)
        self.move_to_front(node)
        return node.val
        # move to the front
    def put(self, key: int, value: int) -> None:
        if self.hashmap.get(key):
            node = self.hashmap[key]
            node.val = value
            self.move_to_front(node)
            return
        node = self.Node(value,key)
        self.add_after_head(node)
        self.hashmap[key] = node
        # print(self.cap)
        # print(len(self.hashmap))
        if len(self.hashmap) > self.cap:
            # print(self.hashmap)
            # print("hi")
            self.evict()
        


        
