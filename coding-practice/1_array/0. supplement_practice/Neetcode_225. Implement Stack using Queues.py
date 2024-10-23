from collections import deque


class MyStack:

    def __init__(self):
        self.push_queue = deque()
        self.pop_queue = deque()

    def push(self, x: int) -> None:
        self.push_queue.append(x)
        for _ in range(len(self.pop_queue)):
            self.push_queue.append(self.pop_queue.popleft())
        self.push_queue, self.pop_queue = self.pop_queue, self.push_queue

    def pop(self) -> int:
        return self.pop_queue.popleft()

    def top(self) -> int:
        return self.pop_queue[0]
        
    def empty(self) -> bool:
        return not self.pop_queue and not self.push_queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())


    def pop(self) -> int:
        return self.queue.popleft()


    def top(self) -> int:
        return self.queue[0]
        
    def empty(self) -> bool:
        return not self.queue
