

# '''
# Linked List hash table key/value pair
# '''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        # Add to count
        self.count += 1

        # Get index based on hash of key
        index = self._hash_mod(key)

        # Get the storage node
        node = self.storage[index]

        # Add KeyValuePair to node
        if node is None:
            self.storage[index] = Node(key, value)
            # Return out of the function
            return

        # Collision handler

        # Iterate to end of node links
        prev = node
        while node is not None:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next
        # Add the values to the node
        prev.next = Node(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # Find index hash of the key
        index = self._hash_mod(key)
        # Open the linked lists at index
        node = self.storage[index]
        prev = None

        # Finds either the requested node or end, whichever first
        while node is not None and node.key != key:
            prev = node
            node = node.next

        # If node is none, key was not found
        if node is None:
            return None
        # Else key was found
        else:
            # Minus count
            self.count -= 1
            # Save the value
            result = node.value
            # Remove the element from the list and repoint the next pointer
            # Exception handler for first value in index
            if prev is None:
                self.storage[index] = None
            # Base Case
            else:
                prev.next = prev.next.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Get the index hash of the key
        index = self._hash_mod(key)

        # Open the linked lists at index position in storage
        node = self.storage[index]

        # Traverse the linked lists to find the key (or end)
        while node is not None and node.key != key:
            node = node.next

        # If node is none, key has not been found.
        if node is None:
            return None
        # Else return the value found
        else:
            return node.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Save the old values
        old_capacity = self.capacity
        old_storage = self.storage
        # Double the capacity
        self.capacity *= 2
        self.storage = [None] * self.capacity

        # Reinsert the values into the new list
        # Iterate across entire index of old storage
        for index in range(old_capacity):
            node = old_storage[index]
            while node is not None:
                key_hldr = node.key
                value_hldr = node.value
                self.insert(key_hldr, value_hldr)
                node = node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
