# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
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
        
        index = self._hash_mod(key)
        
        # Collision handling
        if self.storage[index] is not None:
            next_linked_pair = self.storage[index]
            while next_linked_pair is not None:
                if next_linked_pair.next is None:
                    next_linked_pair.next = LinkedPair(key, value)
                    print("Inserted:", next_linked_pair.next.value)
                    return
                else:
                    next_linked_pair = next_linked_pair.next

            print("Error: Could not insert value")
            return

        else:
            new_node = LinkedPair(key, value)
            self.storage[index] = new_node

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)

        if self.storage[key] is not None:
            self.storage[index] = None 
        else:
            print("Warning: Key not found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)

        if self.storage[index].key != key:

            next_linked_pair = self.storage[index]
            while next_linked_pair is not None:
                if next_linked_pair.key == key:
                    return next_linked_pair.value
                else:
                    next_linked_pair = next_linked_pair.next 

            print("Error: key value not found")
            return

        return self.storage[index].value



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage 
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity
        for item in old_storage:
            self.insert(item.key, item.value)

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print("1.")
    print(ht.retrieve("line_1"))
    print("2.")
    print(ht.retrieve("line_2"))
    print("3.")
    print(ht.retrieve("line_3"))

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print("1.")
    # print(ht.retrieve("line_1"))
    # print("2.")
    # print(ht.retrieve("line_2"))
    # print("3.")
    # print(ht.retrieve("line_3"))

    # print("")