'''Given: A DNA string s of length at most 1000 nt.'''
'''Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur 
# in s'''

s='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
counter_a=s.count('A')
counter_c=s.count('C')
counter_g=s.count('G')
counter_t=s.count('T')
print(counter_a, counter_c, counter_g, counter_t)