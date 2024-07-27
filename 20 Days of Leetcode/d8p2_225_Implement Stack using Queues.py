class MyStack:

    def __init__(self):
        self.push_queue = []
        self.pop_queue = []

    def push(self, x: int) -> None:
        self.push_queue.append(x)

    def pop(self) -> int:
        if not self.pop_queue:
            self.pop_queue.append(self.push_queue.pop())
        return self.pop_queue.pop()

    def top(self) -> int:
        if self.pop_queue:
            return self.pop_queue[-1]
        else:
            return self.push_queue[-1]

    def empty(self) -> bool:
        return not self.push_queue and not self.pop_queue
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()