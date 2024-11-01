'''Given: A positive integer n≤10^5 and an array A[1..n] of integers from −10^5 to 10^5.'''
'''Return: An array B[1..n] such that it is a permutation of A and there are indices 1≤q≤r≤n such that B[i]<A[1]for all 1≤i≤q−1, 
B[i]=A[1]for all q≤i≤r, and B[i]>A[1] for all r+1≤i≤n.'''
n=9
old_a='4 5 6 4 1 2 5 7 4'
tokens_a=old_a.split()
a=[]#initialize list
for i in range(len(tokens_a)):
    values=int(tokens_a[i])
    a.append(values)
b=[]
#this time in the permuted array we'll have 2 points q and r so that from 1 to q-1 there are numbers smaller than the first number
#of a, from q to r all numbers equal to the pivot and from r+1 until the end all the numbers bigger than the pivot
#pivot stays always in the middle
left_partition=[]#that hosts all numbers smaller than our pivot
pivot=a[0]#where a[0]is the first number in the array
for x in a[1:]:
    if x<pivot:
        left_partition.append(x)
mid_partition=[pivot]#that hosts all numbers equal than our pivot, including the pivot
for x in a[1:]:
    if x==pivot:
        mid_partition.append(x)
right_partition=[]#that hosts all numbers smaller or equal to our pivot
for x in a[1:]:
    if x>pivot:
        right_partition.append(x)
b=left_partition+mid_partition+right_partition
print(*b)