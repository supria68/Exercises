#Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

#Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

#Create a funciton which translates a given DNA string into RNA.

dna = input("Enter the string:")

def DNAtoRNA(dna):
    return(dna.upper().replace('T','U'))

rna = DNAtoRNA(dna)
print('This is the rna %s for the given dna %s' %(rna,dna.upper()))
