"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        index = self.calculate_hash_value(string)

        if self.table[index] != None:
            self.table[index].append(string)
        else:
            self.table[index] = [string]

    def lookup(self, string):
        index = self.calculate_hash_value(string)
        value = self.table[index]
        if value != None:
            if string in self.table[index]:
                return index
        return -1

    def calculate_hash_value(self, string):
        first_char = string[0]
        second_char = string[1]

        return (ord(first_char) * 100) + ord(second_char)


# Setup
hash_table = HashTable()

# Test calculate_hash_value
print(hash_table.calculate_hash_value('UDACITY'))  # Should be 8568

# Test lookup edge case
print(hash_table.lookup('UDACITY'))  # Should be -1

# Test store
hash_table.store('UDACITY')
print(hash_table.lookup('UDACITY'))  # Should be 8568

# Test store edge case
hash_table.store('UDACIOUS')
print(hash_table.lookup('UDACIOUS'))  # Should be 8568
