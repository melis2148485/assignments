'''#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind 
allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below'''
fasta_input='''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT'''
#we parse, fasta, sotransform it in a workable form like a dictionary, adding DNA sequence for the current_id in the dictionary.
def parse_fasta(fasta_input):
    fasta_dict={}
    curr_id=None
    for line in fasta_input.splitlines():#splitlines allows to loop thorugh each line in the input, so that the input is broken into
        #lines and when it starts with >, current_id  is assigned on that line
        if line.startswith('>'):
            curr_id = line[1:].strip()  # Extract IDs as keys of dictionary 
            fasta_dict[curr_id] = ''     # Start a new entry in the dictionary
        else:
            fasta_dict[curr_id] += line.strip()  # Add DNA sequence part to current ID as their values
    return(fasta_dict)
#print(fasta_dict)
#Calculate the GC-content of a DNA sequence.
def gc_content(seq):
    return (seq.count('G') + seq.count('C')) / len(seq) * 100
#Find the ID of the sequence with the highest GC-content and its GC-content.
def highest_gc_content(fasta_input):
    fasta_dict = parse_fasta(fasta_input)#to return the dictionary sequences
    max_id = max(fasta_dict.items(), key=lambda item: gc_content(item[1]))[0]#items extract keys of the dictionary, so the sequence IDs
    #and the values, the DNA sequences
#The max() function goes through each item in the dictionary (each sequence), checking the highest GC-content for that sequence,the
# lambda item: gc_content(item[1]) part is a small function that extracts the sequence (item[1] refers to the DNA sequence) 
# and computes its GC-content using the gc_content() function.
    max_gc_content = gc_content(fasta_dict[max_id])
    return max_id, max_gc_content#max_id will get the sequence ID, and max_gc will get the sequence with the highest GC-content.
max_id, max_gc = highest_gc_content(fasta_input)
print(max_id,max_gc)