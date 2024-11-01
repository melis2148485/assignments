'''Given: A positive integer n≤10^5 and an array A[1..n] of integers from −10^5 to 10^5, a positive number k≤n.'''
'''Return: The k-th smallest element of A.'''
n=11
a='2 36 5 21 8 13 11 20 5 4 1'
ref=8
tokens=a.split()
array=[]
for i in range(len(tokens)):
    values=int(tokens[i])
    array.append(values)
def INDEXOFMIN(array,first,last):
    index_min=first
    for k in range(first+1, last+1):
        if array[k]<array[index_min]:
            index_min=k
    return index_min
#index min is defined so that it returns the minimum vale in range c,
def SELECTIONSORT(array):
    n=len(array)
    for i in range (n-1):
        j=INDEXOFMIN(array,i, n-1)
        array[i], array[j]=array[j], array[i]#index of smallest element is found by j, which is the function returning the minimum index and the
        #function swaps the smallest element in the unsorted list with elelment at first position and place it at the start
    return array
new_array=SELECTIONSORT(array)
#print(new_array)
k=new_array[7]
print(k)