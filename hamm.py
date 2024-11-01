'''Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).'''
'''Return: The Hamming distance dH(s,t).'''
s='GAGCCTACTAACGGGAT'
t='CATCGTAATGACGGCCT'
def dH(s,t):
    distance=0
    for i in range(len(s)):
        if s[i]!=t[i]:#checks if characters in same position are diffrent because of the definition of hamming distance, in fact
            distance+=1#if they are different, the distance increases by one for each character, so that in the end the function
    return distance#returns the total number  of corresponding symbols that differ in s and t
print(dH(s,t))
