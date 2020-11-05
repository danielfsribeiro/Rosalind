f = open('rosalind_cons.txt', 'r')
w = open('output.txt', 'w')

s = f.readlines()
sequence = []
temp_seq = ''
#Extract sequence
i=0
while (i < len(s)):
        if s[i][0] != '>':
                temp_seq += s[i].strip()
        else:
                sequence.append(temp_seq)
                temp_seq = ''
        
        i += 1
sequence.append(temp_seq)
sequence.reverse()
sequence.pop()
print(sequence)  
for seq in sequence:
        print(seq)
        print(len(seq))

#Get base and position counts
n = len(sequence[0])
counts = {}
counts['A'] = [0 for i in range(0, n)]
counts['C'] = [0 for i in range(0, n)]
counts['G'] = [0 for i in range(0, n)]
counts['T'] = [0 for i in range(0, n)]

print(sequence)
print(counts)

for seq in sequence:
        #print(len(seq))
        for pos in range(len(seq)):
                counts[seq[pos]][pos] += 1 


print(counts)
#Get consensus
consensus = ''
maxim = 0
base = ''
for pos in range(n):
        for key, value in counts.items():
                if value[pos] > maxim:
                        base = key 
                        maxim = value[pos]
        consensus += base
        base = ''
        maxim = 0

print(consensus)
print('A:', ' '.join('%s' % pos for pos in counts['A'])) 
print('C:', ' '.join('%s' % pos for pos in counts['C'])) 
print('G:', ' '.join('%s' % pos for pos in counts['G'])) 
print('T:', ' '.join('%s' % pos for pos in counts['T'])) 


w.write(consensus + '\n')
w.write(str('A: ' + ' '.join('%s' % pos for pos in counts['A']) + '\n')) 
w.write(str('C: ' + ' '.join('%s' % pos for pos in counts['C']) + '\n'))
w.write(str('G: ' + ' '.join('%s' % pos for pos in counts['G']) + '\n')) 
w.write(str('T: ' + ' '.join('%s' % pos for pos in counts['T']) + '\n')) 
f.close()
w.close()