'''Given: A DNA string s of length at most 1000 bp.'''
'''Return: The reverse complement sc of s.'''
s='AAAACCCGGT'
sc=''
#first create a for loop to substitute each symbol with the complementary one, so A->T and C->G and viceversa
for x in s:
    if x=='A':
        sc+='T'
    elif x=='T':
        sc+='A'
    elif x=='C':
        sc+='G'
    elif x=='G':
        sc+='C'
#reverse sc
print(sc[::-1])