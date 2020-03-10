class DynamicArray:
        #my_array = [4]
        def __init__(self, capacity):
            self.capacity = capacity
            self.count = 0
            self.storage = [None] * self.capacity

        def insert(self, index, value):
             
            # Check capacity
            if self.count >= self.capacity:
                self.double_size()
            
            # Ensure index is in range
            if index > self.count:
                print("Error: index out of range")

            # shift everything over to right
            for i in range(self.count, index, -1):
                self.storage[i] = self.storage[i - 1]
            
            # Insert the value
            self.storage[index] = value 
            self.count += 1

        def append(self, value):
            self.insert(self.count, value)

        def double_size(self):
            self.capacity *= 2
            new_storage = [None] * self.capacity 
            for i in range(0, self.count):
                new_storage[i] = self.storage[i]

            self.storage = new_storage 
 