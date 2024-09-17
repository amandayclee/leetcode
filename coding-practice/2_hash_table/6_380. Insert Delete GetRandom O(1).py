from random import choice


class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.hash_map = {}

    def insert(self, val: int) -> bool:
        if val not in self.hash_map:
            self.hash_map[val] = len(self.lst)
            self.lst.append(val)
            return True  # Successfully inserted
        return False  # Value already exists

    def remove(self, val: int) -> bool:
        if val in self.hash_map:
            lst_idx = self.hash_map[val]
            last_val_in_lst = self.lst[-1]
            
            # Move the last element to the spot of the element to be removed
            self.lst[lst_idx] = last_val_in_lst
            self.hash_map[last_val_in_lst] = lst_idx

            # Remove the last element from the list and the hashmap entry
            self.lst.pop()
            del self.hash_map[val]
            
            return True  # Successfully removed
        return False  # Value not found

    def getRandom(self) -> int:
        return choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()