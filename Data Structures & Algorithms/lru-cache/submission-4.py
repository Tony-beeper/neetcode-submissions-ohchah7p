
class LRUCache:
    class Node:
        def __init__(self, key: int, val: int ):
            self.val = val
            self.next = None
            self.prev = None
            self.key = key

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = self.Node(0,0)
        self.tail = self.Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
    def move_to_head(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.add_after_head(node)

    def add_after_head(self,node):
        next = self.head.next
        self.head.next = node
        next.prev = node
        node.next = next
        node.prev = self.head

    def evict(self):
        last = self.tail.prev
        prev = last.prev
        prev.next = self.tail
        self.tail.prev = prev
        self.hashmap.pop(last.key)

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.move_to_head(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.move_to_head(node)
            return
        new_node = self.Node(key,value)
        self.add_after_head(new_node)
        self.hashmap[key] = new_node
        # self.cap+=1

        if self.cap < len(self.hashmap):
            self.evict()



        


        



        
