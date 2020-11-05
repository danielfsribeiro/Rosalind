f = open('rosalind_iprb.txt', 'r')
w = open('output.txt', 'w')
s = f.readline()

splitted = s.split()
k = float(splitted[0])
m = float(splitted[1])
n = float(splitted[2])
pop = k+m+n
print('k ', k)
print('m ', m)
print('n ', n)
print('pop ', pop)

AA = k
Aa = m
aa = n

#Matings AA first
AAAA = float(AA/pop * ((AA-1)/(pop-1)))
AAAa = float(AA/pop * (Aa/(pop-1)))
AAaa = float(AA/pop * (aa/(pop-1)))
#Matings Aa first
AaAA = float(Aa/pop * (AA/(pop-1)))
AaAa = float(Aa/pop * ((Aa-1.0)/(pop-1)) * (3.0/4)) #3/4 has A allele
Aaaa = float(Aa/pop * (aa/(pop-1)) * (2.0/4)) #2/4 has A allele
#Matings Aa first
aaAA = float(aa/pop * (AA/(pop-1)))
aaAa = float(aa/pop * (Aa/(pop-1)) * (2.0/4)) #2/4 has A allele
aaaa = float(aa/pop * ((aa-1)/(pop-1)) * 0.0)

freq = AAAA + AAAa + AAaa + AaAA + AaAa + Aaaa + aaAA + aaAa + aaaa
print(freq)

w.write(str(freq))
f.close()
w.close()