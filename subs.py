'''Given: Two DNA strings s and t(each of length at most 1 kbp).'''
'''Return: All locations of t as a substring of s.'''
s='GATATATGCATATACTT'
t='ATAT'
positions=0
def str_find(s,t):
    positions=[]
    for i in range (0,len(s)-len(t)+1):#we specify the subtraction because we are iterating over the s string finding the motif of
        #the t string, so the last possible final position is len(s)-len(t) and with +1 to make sure last position is included
        if s[i:i+len(t)]==t:#first position is at zero with the substring 0:4 and the last is 13:17 and loop ends in last possible starting position for t in s string
            positions.append(i+1)
    return(positions)
locations=(str_find(s,t))
print(*locations)
