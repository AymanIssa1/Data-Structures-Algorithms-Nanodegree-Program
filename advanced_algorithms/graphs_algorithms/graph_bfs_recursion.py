class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


def bfs_search(root_node, search_value):
    print("#############Start#############")
    visited = set()
    return bfs_search_start(root_node, visited, search_value)


def bfs_search_start(current_node, visited, search_value):
    print(current_node.value + " ---- > " + str(search_value) + ", visited: " + str(len(visited)))
    if current_node.value == search_value:
        print("found")
        return current_node

    queue = []

    visited.add(current_node)

    result = None

    for node in current_node.children:
        if node not in visited:
            queue.append(node)
            result = bfs_search_start(queue.pop(0), visited, search_value)

    # while len(queue) > 0:
    #     result = bfs_search_start(queue.pop(0), visited, search_value)

    return result


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)

print(bfs_search(nodeS, 'A'))
print(bfs_search(nodeP, 'S'))
print(bfs_search(nodeH, 'R'))
