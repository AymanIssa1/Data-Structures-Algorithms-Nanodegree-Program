import heapq
import sys


class Node(object):

    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_frequency(self, frequency):
        self.frequency = frequency

    def get_frequency(self):
        return self.frequency

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def is_leaf(self):
        return not self.has_right_child() and not self.has_left_child()

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()}, {self.get_frequency()})"

    def __str__(self):
        return f"Node({self.get_value()}, {self.get_frequency()})"

    def __lt__(self, other):
        return self.frequency < other.frequency


class Tree():
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def has_root(self):
        return self.root is not None


def count_frequencies(data):
    map = dict()

    if data is None or len(data) == 0:
        return map

    for c in data:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1
    return map


def create_queue(map):
    queue = []
    for key in map.keys():
        heapq.heappush(queue, (map[key], Node(key, map[key])))
    return queue


def create_huffman_tree(queue):
    tree = None
    # create tree
    while queue:
        if len(queue) == 1:
            tree = Tree(heapq.heappop(queue)[1])
            return tree

        element_1 = heapq.heappop(queue)
        node_1 = element_1[1]
        element_2 = heapq.heappop(queue)
        node_2 = element_2[1]

        new_node = Node((node_1.get_value() + node_2.get_value()),
                        (node_1.get_frequency() + node_2.get_frequency()))

        if node_1.get_frequency() >= node_2.get_frequency():
            new_node.set_right_child(node_1)
            new_node.set_left_child(node_2)
        else:
            new_node.set_right_child(node_2)
            new_node.set_left_child(node_1)

        heapq.heappush(queue, (new_node.get_frequency(), new_node))


def huffman_encoding(data):
    # counting chars
    map = count_frequencies(data)

    # inserting chars into binary heap
    queue = create_queue(map)

    tree = create_huffman_tree(queue)

    codes_table = create_huffman_table(tree)
    print(codes_table)

    encode = create_encode(codes_table, data)
    print(encode)

    return encode, tree


def create_huffman_table(tree):
    codes_table = {}

    if tree is None or not tree.has_root():
        return codes_table

    get_code(codes_table, tree.get_root(), "")
    return codes_table


def get_code(codes_table, node, current_code=""):
    if node is None:
        return
    if node.is_leaf():
        codes_table[node.value] = current_code

    get_code(codes_table, node.get_left_child(), current_code + '0')
    get_code(codes_table, node.get_right_child(), current_code + '1')


def create_encode(codes_table, data):
    encode = ""

    if data is None or len(data) == 0:
        return "0"

    for char in data:
        encode += codes_table[char]

    if len(encode) == 0:
        return "0"

    return encode


def huffman_decoding(data, tree):
    decoded = ""

    if tree is None or not tree.has_root():
        return decoded

    node = tree.get_root()
    for char in data:
        if char == "0":
            node = node.get_left_child()
        elif char == "1":
            node = node.get_right_child()

        if node.is_leaf():
            decoded += node.get_value()
            node = tree.get_root()

    return decoded


# data, tree = huffman_encoding("AAAAAAABBBCCCCCCCDDEEEEEE")
# print(huffman_decoding(data, tree))

if __name__ == "__main__":
    codes = {}

    # Case 1
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Case 2
    a_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Case 2
    a_great_sentence = None

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
