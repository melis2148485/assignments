'''Given: A positive integer n≤105 and array A[1..n] of integers from −10^5 to 10^5.'''
'''Return: A permuted array A satisfying the binary max heap property: for any 2≤i≤n, A[⌊i/2⌋]≥A[i].'''
n=5
a='1 3 5 7 2'
#In a max heap, each parent node has a value greater than or equal to its child nodes. Here's a breakdown of how this 
# code works in the context of your assignment.
tokens=a.split()
array=[]#initialize list
for i in range(len(tokens)):
    values=int(tokens[i])
    array.append(values)

def create_heap(array):
    heap = [0]  # Initialize heap with a dummy zero to simplify indexing:Adding this dummy 0 allows for simpler calculations 
#of parent and child indices in the array, as the parent of any node i can be found at i // 2 and children at 2 * i and 2 * i + 1.
    for value in array:
        heap.append(value)  # Add each element to the heap
        index = len(heap) - 1  # gives index to the newly added element's position, remembering that when a new value is appended 
        #to heap, it is added at the end of the list, 
        #By setting index to len(heap) - 1, we are pointing to this new element, allowing us to start the "sifting up"process from this 
# position.
#to maintain the max-heap property as we add new elements. In a max heap, every parent node should be larger than its child nodes
        while heap[index // 2] < heap[index] and index // 2 > 0:#we check if the newly added element 
            #(heap[index]) is larger than its parent node (heap[index // 2]),assuming we don't go above the root node
            # (the root's "parent" would be heap[0]
            heap[index], heap[index // 2] = heap[index // 2], heap[index]#if the added element is larger, we swap it with the parent
            #so that it moves up in the heap, repscting the max heap property
            index = index // 2
    return heap[1:]#TO REMOVE DUMMY VARIABLE 0
print(create_heap(array))
