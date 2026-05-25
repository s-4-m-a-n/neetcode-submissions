class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    
class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr_node = self.head.next_node
        i = 0
        while curr_node:
            if i == index:
                return curr_node.value
            i += 1
            curr_node = curr_node.next_node
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head.next_node)
        self.head.next_node = new_node
        if not new_node.next_node:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next_node = new_node
        self.tail = new_node
            
    def remove(self, index: int) -> bool:
        curr_node = self.head
        i = 0 
        while i < index and curr_node:
            curr_node = curr_node.next_node
            i += 1
        
        if curr_node and curr_node.next_node:
            if curr_node.next_node == self.tail:
                self.tail = curr_node
            curr_node.next_node = curr_node.next_node.next_node
            return True
        return False
        
    def getValues(self) -> List[int]:
        values = []
        node = self.head.next_node
        while node:
            values.append(node.value)
            node = node.next_node
        return values