class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.length = 0

    def get(self, i: int) -> int:
        for idx in range(self.length):
            if idx == i:
                return self.arr[idx]

    def set(self, i: int, n: int) -> None:
        for idx in range(self.length):
            if idx == i:
                self.arr[idx] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        temp = self.arr[self.length - 1]
        self.arr[self.length - 1] = 0
        self.length -= 1

        return temp

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_array = [0] * self.capacity

        for i in range(self.length):
            new_array[i] = self.arr[i]
        self.arr = new_array

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
