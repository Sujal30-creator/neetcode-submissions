class MyQueue:

    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def push(self, x: int) -> None:
        self.s2.append(x)
        if self.s1:
            self.s2.extend(self.s1)
            self.s1.clear()
        self.s1, self.s2 = self.s2, self.s1
        

    def pop(self) -> int:
        return self.s1.pop()
        

    def peek(self) -> int:
        return self.s1[len(self.s1)-1]
        

    def empty(self) -> bool:
        return not self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()