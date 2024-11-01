'''Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).'''
'''Return: The protein string encoded by s.'''
s='AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
rna_codon_table='''
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G '''
#we transform the rna codon table into a dctionary where the keys are the triplets and the values is the symbol of the corresponding
#protein
tokens=rna_codon_table.split()
rna_codon_dict={}
for i in range(0,len(tokens),2):#by 2 we want the loop to work with 2 items at a time, so the triplet and the amino acid symbol
    codons=tokens[i]
    amino_acid=tokens[i+1]
    rna_codon_dict[codons]=amino_acid
s_protein=''
for i in range(0,len(s), 3):#code reads through each codon, a set of 3 rna bases in the rna sequence
    if rna_codon_dict[s[i:i+3]]!='Stop':#[s[i:i+3]]!='Stop' means that for each 3-base segment, if the aminoacid is not stop, the
        #aminoacid is added to the s_protein(all stop codons are skipped)
        s_protein += rna_codon_dict[s[i:i+3]]
print(s_protein)
#explanation: