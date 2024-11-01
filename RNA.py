'''Given: A DNA string t having length at most 1000 nt.'''
'''Return: The transcribed RNA string of t.'''
t='GATGGAACTTGACTACGTAAATT'
transcr_RNA = ''
for char in t:
    if char == 'T':
        transcr_RNA += 'U'
    else:
        transcr_RNA += char
print(transcr_RNA)