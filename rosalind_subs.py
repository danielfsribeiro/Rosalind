f = open('rosalind_subs.txt', 'r')
w = open('output.txt', 'w')

#s = 'GATATATGCATATACTT'
#t = 'ATAT'
#2 4 10
s = f.readline().strip()
print(s)
t = f.readline().strip()
print(t)

positions = []
pos = 0
start = 0
found = s.find(t, start, len(s))
print(found)
while (found != -1):
        positions.append(str(found+1))
        start = found+1
        found = s.find(t, start, len(s))
        print(found)

answer = ' '.join(positions)

print(answer)
w.write(answer)
f.close()
w.close()