'''Given: A positive integer n≤10^5 and an array A[1..n] of integers from −10^5 to 10^5.'''
'''Return: A sorted array A[1..n].'''
n=7
old_a='5 -2 4 7 8 -10 11'
tokens_a=old_a.split()
a=[]#initialize list
for i in range(len(tokens_a)):
    values=int(tokens_a[i])
    a.append(values)
sorted_a=sorted(a)
print(sorted_a)