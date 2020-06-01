import hashlib
from datetime import datetime


class Node:
    def __init__(self, block):
        self.block = block
        self.next = None


def calc_hash():
    sha = hashlib.sha256()

    hash_str = "We are going to encode this string of data!".encode('utf-8')

    sha.update(hash_str)

    return sha.hexdigest() + str(getTimestamp())


def getTimestamp():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return timestamp


class Block:

    def __init__(self, timestamp, data, previous_hash, hash=calc_hash()):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = hash

    def __str__(self):
        return f"Block({self.timestamp}, {self.data}, {self.previous_hash}, {self.hash})"



class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addBlock(self, value, hash=calc_hash()):
        if self.head is None:
            node = Node(Block(getTimestamp(), value, None, hash))
            self.head = node
            self.tail = node
        else:
            node = Node(Block(getTimestamp(), value, self.tail.block.hash, hash))
            self.tail.next = node
            self.tail = self.tail.next

        self.size += 1

    def get_size(self):
        return self.size

    def get_block_by_index(self, index):
        if index < 0 or self.size == 0:
            return None

        if index == 0:
            return self.head

        if index == self.size:
            return self.head

        requested_node = self.head
        current_index = 0
        while requested_node is not None:
            if current_index == index:
                return requested_node.block

            current_index += 1
            requested_node = requested_node.next

        return None

    def get_block_by_hash(self, hash):
        if hash is None or len(hash) == 0:
            return None

        request_node = self.head
        while request_node is not None:
            if request_node.block.hash == hash:
                return request_node.block
            request_node = request_node.next

        return None

    def print_all(self):
        node = self.head
        total = ""
        while node is not None:
            total += str(node.block.data) + " -> "
            node = node.next

        print(total)


block_chain = BlockChain()
block_chain.addBlock(0)
block_chain.addBlock(1)
block_chain.addBlock(2, "asodkqwekd-aksd-1ik23- ksdfkasd")
block_chain.addBlock(3)
block_chain.addBlock(4)
block_chain.addBlock(5)

print(block_chain.get_block_by_index(3))
print(block_chain.get_block_by_hash("asodkqwekd-aksd-1ik23- ksdfkasd"))
print(block_chain.get_block_by_hash(""))
print(block_chain.get_block_by_hash(None))

block_chain.print_all()
