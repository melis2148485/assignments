'''Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous 
dominant for a factor, m are heterozygous, and n are homozygous recessive'''
'''Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.'''

#since any orgnism can mate, we have 6 possible combinations, in which organisms can be of same tyoe or different
#function is about probability of having an individual with a dominant allele

def prob_dominant(k,m,n):
    total=k+m+n 
    total_pairs=total*(total-1)
    #calculate probability of dominant offspring for each pair
    kk_pair=k*(k-1) #2 homozygous dominant organisms and probability is equal 1 because both are dominant
    km_pair=k*m #1 homozygous dominant with 1 heterozygous
    kn_pair=k*n #1 homozygous dominant with 1 homozygous recessive
    mm_pair=m*(m-1)*0.75 #2 heterozygous dominant organisms and probability of producing dominant phenotype is 0.75
    mn_pair=m*n*0.5#1 heterozygous dominant with 1 homozygous recessive and probability of producing a dominant phenotype is 0.5
    nn_pair=0 #can't obtain a dominant allele because both factors are homozygous recessive
    #sum probabilities, since they are mutually exclusive
    dominant_outcome=kk_pair+2*km_pair+2*kn_pair+mm_pair+2*mn_pair
    fin_prob_dominant=dominant_outcome/total_pairs
    return fin_prob_dominant
k=2  
m=2
n=2
result=prob_dominant(k,m,n)
print(result)
