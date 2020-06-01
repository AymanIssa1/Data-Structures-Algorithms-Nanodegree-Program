from collections import deque


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.storage = dict()
        self.storage_keys_order = deque()
        self.num_of_elements = 0

    def get(self, key):
        if self.capacity <= 0 or key not in self.storage:
            return -1

        self.storage_keys_order.remove(key)
        self.storage_keys_order.append(key)
        return self.storage[key]

    def set(self, key, value):
        if self.capacity <= 0:
            return

        # Set the value if the key is not present in the cache. If the cache reached the capacity remove the oldest item.
        if self.num_of_elements >= self.capacity:
            oldest_key = self.storage_keys_order.popleft()
            self.storage.pop(oldest_key)
            self.num_of_elements -= 1

        self.num_of_elements += 1
        self.storage_keys_order.append(key)
        self.storage[key] = value


# Test Case 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache
print(our_cache.get(None))  # return -1

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
print(our_cache.get(4))

# Test Case 2
our_cache2 = LRU_Cache(10)

our_cache2.set(1, 61435)
our_cache2.set(2, 234123)
our_cache2.set(3, 651234)
our_cache2.set(4, 1234123)
our_cache2.set(6, 465234)
our_cache2.set(7, 1231234)
our_cache2.set(8, 1342341)
our_cache2.set(9, 5634)
our_cache2.set(10, 123)

print(our_cache2.get(1))
print(our_cache2.get(2))
print(our_cache2.get(4))
print(our_cache2.get(5))
print(our_cache2.get(6))
print(our_cache2.get(7))

our_cache2.set(5, 5)
our_cache2.set(6, 6)

print(our_cache2.get(3))

# Test Case 3
our_cache3 = LRU_Cache(0)

our_cache3.set(1, 61435)
our_cache3.set(2, 234123)
our_cache3.set(3, 651234)

print(our_cache3.get(1))
print(our_cache3.get(2))
print(our_cache3.get(3))

our_cache3.set(1, 5)
our_cache3.set(2, 6)

print(our_cache3.get(3))
