I have used Trie structure to store set of strings and I  am using Trie class to solve this problem.

RouteTrie insert method has time complexity and space complexity of O(n). where n = number of routes
RouteTrie find method has time complexity and space complexity of O(n). where n = number of routes

RouteTrieNode insert method has time complexity and space complexity of O(1).


Router split_path method has time complexity of O(n) and space complexity of O(n). where n = number of routes
Router lookup method time and space complexity = Router split_path + RouteTrie find
Router add_handler method time and space complexity = Router split_path + RouteTrie insert