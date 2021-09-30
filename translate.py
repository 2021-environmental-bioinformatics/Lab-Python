#!/user/bin/env python3
import sys

codon_dict = {}
with open('data/std-code.tab') as f:
    for line in f:
        line = line.strip()
        s = line.split(' ')
        codon_dict[s[0]] = s[1]

def get_protein(sequence='ACTGTCAAAAAT'):
    protein = ''
    for i in range(0,len(sequence), 3):
        codon = sequence[i:i+3]
        protein += codon_dict[codon]
    return(protein)    

if __name__=='__main__':
    out_protein = get_protein(sys.argv[1])
    print('The sequence {} can be translated to {}'.format(sys.argv[1],out_protein))
