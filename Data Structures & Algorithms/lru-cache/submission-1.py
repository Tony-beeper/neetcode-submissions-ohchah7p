class LRUCache:
    class Node:
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
    def __init__(self, capacity: int):
        self.map = {}
        self.cap = capacity
        self.head = self.Node(0,0)
        self.tail = self.Node(0,0)
        self.head.next_node = self.tail
        self.head.prev_node = None
        self.tail.next_node = None
        self.tail.prev_node = self.head

    def add_after_head(self, node):
        buf = self.head.next_node
        self.head.next_node = node
        node.next_node = buf
        node.prev_node = self.head
        buf.prev_node = node

    def move_to_head(self, node):
        prev_node, next_node = node.prev_node, node.next_node
        prev_node.next_node = next_node
        next_node.prev_node = prev_node
        self.add_after_head(node)

    def pop_lru(self):
        # print(self.map)
        # while self.head.next_node:
        #     print(self.head.next_node.val)
        #     self.head = self.head.next_node
        # print(self.tail.prev_node.prev_node.val)
        popper = self.tail.prev_node
        # print(popper.key)
        popper.prev_node.next_node = self.tail
        self.tail.prev_node = popper.prev_node
        self.map.pop(popper.key, None)



    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node:
            self.move_to_head(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:

        node = self.map.get(key)
        if node:
            node.val = value
            self.move_to_head(node)
            return
        node = self.Node(key,value)
        self.map[key] = node
        self.add_after_head(node)
        # evict
        if len(self.map) > self.cap:
            self.pop_lru()
        return
        

        
