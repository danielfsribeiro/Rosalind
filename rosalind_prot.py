f = open('rosalind_prot.txt', 'r')
w = open('output.txt', 'w')

#s = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
s = f.readline()

#Genetic code
genetic_code = {  'UUU' : 'F',      'CUU' : 'L',      'AUU' : 'I',      'GUU' : 'V',
'UUC' : 'F',      'CUC' : 'L',      'AUC' : 'I',      'GUC' : 'V',
'UUA' : 'L',      'CUA' : 'L',      'AUA' : 'I',      'GUA' : 'V',
'UUG' : 'L',      'CUG' : 'L',      'AUG' : 'M',      'GUG' : 'V',
'UCU' : 'S',      'CCU' : 'P',      'ACU' : 'T',      'GCU' : 'A',
'UCC' : 'S',      'CCC' : 'P',      'ACC' : 'T',      'GCC' : 'A',
'UCA' : 'S',      'CCA' : 'P',      'ACA' : 'T',      'GCA' : 'A',
'UCG' : 'S',      'CCG' : 'P',      'ACG' : 'T',      'GCG' : 'A',
'UAU' : 'Y',      'CAU' : 'H',      'AAU' : 'N',      'GAU' : 'D',
'UAC' : 'Y',      'CAC' : 'H',      'AAC' : 'N',      'GAC' : 'D',
'UAA' : 'Stop',   'CAA' : 'Q',      'AAA' : 'K',      'GAA' : 'E',
'UAG' : 'Stop',   'CAG' : 'Q',      'AAG' : 'K',      'GAG' : 'E',
'UGU' : 'C',      'CGU' : 'R',      'AGU' : 'S',      'GGU' : 'G',
'UGC' : 'C',      'CGC' : 'R',      'AGC' : 'S',      'GGC' : 'G',
'UGA' : 'Stop',   'CGA' : 'R',      'AGA' : 'R',      'GGA' : 'G',
'UGG' : 'W',      'CGG' : 'R',      'AGG' : 'R',      'GGG' : 'G'}

translate = ''
codon = ''
for i in range(0, len(s)-3, 3):
    codon = ''.join([s[i], s[i+1], s[i+2]])
    print(codon)
    if genetic_code[codon] != 'Stop':
        translate += genetic_code[codon]
        print (genetic_code[codon])

print(translate)

w.write(translate)
f.close()
w.close()