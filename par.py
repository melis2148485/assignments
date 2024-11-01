'''Given: A positive integer n≤10^5 and an array A[1..n of integers from −10^5 to 10^5.'''
'''Return: A permuted array B[1..n] such that it is a permutation of A and there is an index 1≤q≤n such that B[i]≤A[1] for all 
# 1≤i≤q−1, B[q]=A[1], and B[i]>A[1] for all q+1≤i≤n.'''
n=9
old_a='7 2 5 6 1 3 9 4 8'
tokens_a=old_a.split()
a=[]#initialize list
for i in range(len(tokens_a)):
    values=int(tokens_a[i])
    a.append(values)
b=[]
#the permuted array must be built so that we have a point q to put a[1], with numbers on left smaller or equal to a[1]and numbers
#on the right bigger than a[1],so
left_partition=[]#that hosts all numbers smaller or equal to our pivot
pivot=a[0]#where a[0]is the first number in the array
for x in a[1:]:
    if x<=pivot:
        left_partition.append(x)
right_partition=[]#that hosts all numbers smaller or equal to our pivot
for x in a[1:]:
    if x>pivot:
        right_partition.append(x)
b=left_partition+[pivot]+right_partition
print(*b)