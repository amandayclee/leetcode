class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hash_table = [None] * capacity

    def _hashing(self, key):
        index = 0
        for i, c in enumerate(str(key)):
            index += ord(c) * (31 ** i)
        return index % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self._hashing(key)
        original_index = index

        while True:
            if self.hash_table[index] is None:
                self.hash_table[index] = Pair(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.resize()
                return
            elif self.hash_table[index].key == key:
                self.hash_table[index].value = value
                return
            
            index = (index + 1) % self.capacity
            if index == original_index:
                break

    def get(self, key: int) -> int:
        index = self._hashing(key)
        original_index = index

        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                return self.hash_table[index].value
            index = (index + 1) % self.capacity
            if index == original_index:
                break
        return -1

    def remove(self, key: int) -> bool:
        index = self._hashing(key)
        original_index = index

        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                self.hash_table[index] = None
                self.size -= 1
                return True
            
            index = (index + 1) % self.capacity
            if index == original_index:
                break
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_table = self.hash_table[:]
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        self.size = 0

        for pair in old_table:
            if pair is not None:
                self.insert(pair.key, pair.value)