# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        # self.handler = handler

    def insert(self, path_list, handler):
        current_node = self.root

        for next_path in path_list:
            current_node = current_node.insert(next_path)

        current_node.handler = handler

    def find(self, path_list):
        current_node = self.root

        for next_path in path_list:

            if next_path not in current_node.children:
                return None

            current_node = current_node.children[next_path]

        return current_node


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

    def insert(self, path):
        if path in self.children:
            current_node = self.children[path]
        else:
            new_node = RouteTrieNode()
            self.children[path] = new_node
            current_node = new_node

        return current_node


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.routeTrie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        route = self.routeTrie.find(self.split_path(path))
        if route is None:
            return self.not_found_handler

        return route.handler

    def split_path(self, path):
        list = path.split('/')
        filtered_list = []
        for item in list:
            if item != '':
                filtered_list.append(item)
        return filtered_list


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
