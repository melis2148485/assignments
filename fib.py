'''Given: Positive integers n≤40 and k≤5.'''
'''Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, 
every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).'''
n=5 #n=months
k=3#n of rabbit pairs produced over n
def fib ( n,k ) :
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fib (n -1,k) + fib (n -2,k)*k
print(fib(n,k))
##fib_rabbits(n - 1, k): term includes all the rabbits that were alive in the previous month.
##k * fib_rabbits(n - 2, k):represents the number of mature rabbit pairs from two months ago, including  the rabbit pairs 
# were alive and also mature enough to reproduce, considering k pairs of new rabbits born for the previous months