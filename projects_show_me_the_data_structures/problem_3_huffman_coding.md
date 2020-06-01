I have used directory to count frequnces then I have used heapq to priortize the elements from lowest frequency to highest one. 
after that i was popping 2 nodes from the queue (list) then merge them into small tree till i created huffman tree.
afterwords I created huffman codes table by traversing through the tree.

after that I created the encoded codes.

and for decoding I just traversed again into the tree using 0s and 1s till i reached a leap so i can decode the data

encoding analysis: O(nlogn) time and O(n) space 

    - count_frequencies require O(n) time and space
    - create_queue require O(n) time and space
    - create_huffman_tree require O(n) time and space
        Note: heappush and heappop in heapq are O(1)
    - create_huffman_table require O(n*d) time and O(n) space where d = depth of the tree
    - create_encode require O(n) time and space
    
    
decoding analysis:

    - huffman_decoding require O(n*d) time and O(n) space where d = depth of the tree