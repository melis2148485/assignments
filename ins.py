'''Given: A positive integer n≤10^3 and an array A[1..n] of integers.'''
'''Return: The number of swaps performed by insertion sort algorithm on A[1..n].'''
n=6
old_a='6 10 4 5 1 2'
tokens=old_a.split()
a=[]#initialize list
for i in range(len(tokens)):
    values=int(tokens[i])
    a.append(values)
#print(a)
swap_count=0#initialize counter
for i in range (1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and key <a[j]:#putting them in order by swapping them
        a[j+1]=a[j]
        j-=1
        swap_count+=1
    a[j+1]=key

print(swap_count)
