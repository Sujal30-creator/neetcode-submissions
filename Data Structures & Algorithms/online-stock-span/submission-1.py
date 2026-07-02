class StockSpanner:

    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        counter = 1
        if not self.stack:
            self.stack.append([price, counter])
        else:
            while self.stack and price>=self.stack[-1][0]:
                stackPrice, stackCounter = self.stack.pop()
                counter += stackCounter
                
            self.stack.append([price, counter])
        return counter


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)