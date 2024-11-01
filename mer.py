'''Given: A positive integer n≤10^5 and a sorted array A[1..n] of integers from −10^5 to 10^5, a positive integer m≤10^5
and a sorted array B[1..m] of integers from −10^5 to 10^5.'''
'''Return: A sorted array C[1..n+m] containing all the elements of A and B.'''
n=4
old_a='2 4 10 18'
m=3
old_b='-5 11 12'
tokens_a=old_a.split()
a=[]#initialize list
for i in range(len(tokens_a)):
    values=int(tokens_a[i])
    a.append(values)
tokens_b=old_b.split()
b=[]#initialize list
for i in range(len(tokens_b)):
    values=int(tokens_b[i])
    b.append(values)
#concatenate a and b in c
def INDEXOFMIN(c,first,last):
    index_min=first
    for k in range(first+1, last+1):
        if c[k]<c[index_min]:
            index_min=k
    return index_min
#index min is defined so that it returns the minimum vale in range c,
c=a+b
def SELECTIONSORT(c):
    n=len(c)
    for i in range (n-1):
        j=INDEXOFMIN(c,i, n-1)
        c[i], c[j]=c[j], c[i]#index of smallest element is found by j, which is the function returning the minimum index and the
        #function swaps the smallest element in the unsorted list with elelment at first position and place it at the start
    return c
first=0
last=len(c)-1
sorted_c=(SELECTIONSORT(c))
print(*sorted_c)
