'''Given: A positive integer n≤10^5 and an array A[1..n] of integers from −10^5 to 10^5, a positive integer k≤1000.'''
'''Return: The k smallest elements of a sorted array A.'''
n=10
a='4 -6 7 8 -9 100 12 13 56 17'
k=3
tokens=a.split()
array=[]#initialize list
for i in range(len(tokens)):
    values=int(tokens[i])
    array.append(values)
k_min=sorted(array)[:k]
print(*k_min)