'''Given: A positive integer n≤10^5 and an array A[1..n] of integers from −10^5 to 10^5.'''
'''Return: A sorted array A.'''

#we create the max heap array, this time sorting a so that we respect te rule for the binary heap plus the array is sorted
#in the correct order
n=9
a='2 6 7 1 3 5 4 8 9'
tokens=a.split()
array=[]
for i in range(len(tokens)):
    values=int(tokens[i])
    array.append(values)

def check_heap(array, heap_size,v):
    while True:
        max_node=v
        if v*2+1<heap_size and array[v*2+1]>array[max_node]:#checking if left child exists and is greater than the current max node
            max_node=v*2+1#if so, update max node as the left child is greater
        if v*2+2<heap_size and array[v*2+2]>array[max_node]:#checking if right child exists and is greater than the current max node
            max_node=v*2+2##if so, update max node as the right child is greater
        if max_node==v:
            break
        array[v], array[max_node]=array[max_node],array[v]#maintain max heap by swapping values if necessary
        v=max_node#move down to continue to check
def build_max_heap(array):
    for i in range(len(array)-1,0,-1):#we move backward from the last element added, excluding 0
        parent=(i-1)//2
        if array[i]>array[parent]:
            array[parent],array[i]=array[i], array[parent]#swap positions if child node is greater
            check_heap(array, len(array),i)
    return(array)
def heap_sort(array):
    build_max_heap(array)
    for heap_size in range(len(array),1,-1):#to extract each element one by one
        array[0], array[heap_size-1]=array[heap_size-1],array[0]#swap root and last element, then restore max heap for reduced heap
        check_heap(array,heap_size-1,0)
    return array
#function of the loop is starting at the normal sze of the heap, each time the loop iterates, its size decreases by 1:loop is 
#reduced by 1 element at each step, as each time the largest element is removed and placed at the end of the sorted portion of the array
fin_arr=(heap_sort(array))
print(*fin_arr)