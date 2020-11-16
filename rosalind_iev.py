f = open('rosalind_iev.txt', 'r')
w = open('output.txt', 'w')

# 1. AAxAA = [1.0, 0, 0] #[AA, Aa, aa]
# 2. AAxAa
# 3. AAxaa
# 4. AaxAa
# 5. Aaxaa
# 6. aaxaa 
genotype_probability = {
    1: [1.0, 0.0, 0.0],
    2: [0.5, 0.5, 0.0],
    3: [0.0, 1.0, 0.0],
    4: [0.25, 0.5, 0.25],
    5: [0.0, 0.5, 0.5],
    6: [0.0, 0.0, 1.0]
}

genotypes = [0.0, 0.0, 0.0]

data = f.readline().split()
pops = [int(pop) for pop in data]
print(pops)

for key, val in genotype_probability.items():
    genotypes[0] = genotypes[0] + (val[0] * pops[key - 1]) * 2  #Calc AA genotype
    genotypes[1] = genotypes[1] + (val[1] * pops[key - 1]) * 2  #Calc Aa genotype
    genotypes[2] = genotypes[2] + (val[2] * pops[key - 1]) * 2  #Calc aa genotype
print(genotypes)

w.write(str(genotypes[0] + genotypes[1]))

f.close()
w.close()