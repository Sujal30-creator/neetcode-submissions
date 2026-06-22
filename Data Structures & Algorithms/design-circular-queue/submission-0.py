class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        
    def enQueue(self, value: int) -> bool:
        if self.size < self.capacity:
            if self.size == 0:
                self.start = Node(value)
                self.end = self.start
            else:
                self.end.next = Node(value)
                self.end.next.prev = self.end
                self.end = self.end.next

            self.start.prev = self.end
            self.end.next = self.start
            self.size += 1 
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.size == 1:
            self.size -= 1
            self.start = None
            self.end = None
        elif self.size > 1:
            self.start.next.prev = self.end
            self.end.next = self.start.next
            self.start = self.start.next
            self.size -= 1
        else:
            return False
        return True

    def Front(self) -> int:
        if self.size:
            return self.start.value
        return -1

    def Rear(self) -> int:
        if self.size:
            return self.end.value
        return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        return False