f = open('rosalind_grph.txt', 'r')
w = open('output.txt', 'w')


sequences = {}
name = ''
seq = ''

for line in f:
    l = line.strip()
    if l[0] == '>':
        name = l[1:]
    else:
        seq = l
        sequences[name] = seq
        name = ''
        seq = ''
print(sequences)

result = []
for key, val in sequences.items():
    for key2, val2 in sequences.items():
        if val != val2 and val[-3:] == val2[:3]:
            result.append((key, key2))

for item in result:
    w.write(' '.join(item) + '\n')
    

f.close()
w.close()