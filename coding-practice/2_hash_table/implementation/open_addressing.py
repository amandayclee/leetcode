from typing import Any, Optional, List, Tuple


class HashMapOpenAddressing:
    """
    A simple implementation of a hash map using open addressing
    with double hashing for collision resolution.
    """

    def __init__(self, size: int = 10) -> None:
        """
        Initializes the hash map with a specified size.

        Args:
            size (int): The initial size of the hash table.
        """
        self.size = size
        self.table: List[Optional[Tuple[Any, Any]]] = [None] * size
        self.load_factor = 0.7
        self.count = 0

    def _hash_primary(self, key: Any) -> int:
        """
        Primary hash function.

        Args:
            key: The key to be hashed.

        Returns:
            int: The primary hash index.
        """
        return hash(key) % self.size

    def _hash_secondary(self, key: Any) -> int:
        """
        Secondary hash function for double hashing.

        Args:
            key: The key to be hashed.

        Returns:
            int: The secondary hash step size.
        """
        return 1 + (hash(key) % (self.size - 1))

    def _rehash(self) -> None:
        """
        Rehashes the table when the load factor exceeds the threshold.
        """
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        for item in old_table:
            if item and item[0] is not None:
                self.insert(item[0], item[1])

    def insert(self, key: Any, value: Any) -> None:
        """
        Inserts a key-value pair into the hash map.

        Args:
            key: The key to be inserted.
            value: The value to be associated with the key.
        """
        if self.count / self.size > self.load_factor:
            self._rehash()

        index = self._hash_primary(key)
        step = self._hash_secondary(key)
        # print(f"Inserting key: {key}, initial index: {index}, step: {step}")
        # Loop to handle collisions using double hashing
        while self.table[index] is not None and self.table[index][0] is not None:
            # If the key already exists, update its value and return
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            # Calculate the next index using the secondary hash step size
            index = (index + step) % self.size
            # print(f"Collision occurred, new index: {index}")

        # Insert the new key-value pair at the calculated index
        self.table[index] = (key, value)
        self.count += 1


    def delete(self, key: Any) -> None:
        """
        Deletes a key-value pair from the hash map.

        Args:
            key: The key to be deleted.
        """
        index = self._hash_primary(key)
        step = self._hash_secondary(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (None, None)
                self.count -= 1
                return
            index = (index + step) % self.size

    def search(self, key: Any) -> Optional[Any]:
        """
        Searches for a value associated with a key in the hash map.

        Args:
            key: The key to search for.

        Returns:
            Optional[Any]: The value associated with the key, or None if the key is not found.
        """
        index = self._hash_primary(key)
        step = self._hash_secondary(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + step) % self.size
        return None


# Example usage of HashMapOpenAddressing
if __name__ == "__main__":
    # Create a new hash map
    hash_map = HashMapOpenAddressing(size=10)

    # Insert key-value pairs
    hash_map.insert("apple", 1)
    hash_map.insert("banana", 2)
    hash_map.insert("cherry", 3)

    # Search for values
    print(hash_map.search("apple"))  # Output: 1
    print(hash_map.search("banana"))  # Output: 2
    print(hash_map.search("cherry"))  # Output: 3
    print(hash_map.search("date"))  # Output: None (not found)

    # Update a value
    hash_map.insert("banana", 20)
    print(hash_map.search("banana"))  # Output: 20

    # Delete a key-value pair
    hash_map.delete("apple")
    print(hash_map.search("apple"))  # Output: None (deleted)

    # Insert more key-value pairs to trigger rehashing
    for i in range(4, 15):
        hash_map.insert(f"key{i}", i)

    # Check values after rehashing
    print(hash_map.search("key10"))  # Output: 10
    print(hash_map.search("key14"))  # Output: 14
