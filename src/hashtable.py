# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        return hash(key)


    def _hash_djb2(self, key):
        pass


    def _hash_mod(self, key):
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        index = self._hash_mod(key) # Get index of key's hash

        if not self.retrieve(key) == None: # If key in storage, remove it
            self.remove(key)

        if self.storage[index] == None: # If empty slot, insert value
            self.storage[index] = LinkedPair(key, value)
        else: # Otherwise, go through all nodes until there's no next node
            node = self.storage[index]
            while node.next:
                node = node.next
            node.next = LinkedPair(key, value) # Insert at end of the last node


    def remove(self, key):
        index = self._hash_mod(key) # Get index of key's hash
        if self.storage[index] == None: # Can't remove empty index
            return
        else: # Go through all nodes
            node = self.storage[index]
            node_prev = None
            while node:
                if node.key == key: # If found key
                    if node_prev: # Set previous node's next to this node's next
                        node_prev.next = node.next
                    else:
                        self.storage[index] = None # Otherwise, remove it enitrely
                    return
                node_prev = node
                node = node.next


    def retrieve(self, key):
        index = self._hash_mod(key)  # Get index of key's hash
        if self.storage[index] == None: # If empty index, return None
            return None
        else:
            node = self.storage[index] # Go through all nodes
            while node:
                if node.key == key:
                    return node.value # Return value if found
                node = node.next
        return None


    def resize(self):
        self.capacity *= 2 # Double capacity
        temp = [] # Keep temp array with key-value pairs
        for i in self.storage:
            if not i == None:
                node = i 
                while node:
                    temp.append((node.key, node.value)) # Add pairs to array
                    node = node.next
        self.storage = [None] * self.capacity # Make new storage array
        for pair in temp:
            self.insert(pair[0], pair[1])  # Insert all the pairs back in



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
