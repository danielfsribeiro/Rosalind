f = open('rosalind_fibd.txt', 'r')
w = open('output.txt', 'w')
s = f.readline().strip()

print(s)
#Test
#f = "6 3"

month = int(s.split()[0])
lifespan = int(s.split()[1])
print(month, lifespan)

def rabbits(months: int, life: int) -> tuple:
    print(months, life)
    if months <= 0:
        return 0, 0, 0
    elif months == 1:
      newborns = 1
      adults = 0
      return newborns, adults, newborns + adults
    else:
        res = rabbits(months-1, life)
        newborns = res[1]
        adults = newborns + res[0] - rabbits(months-life, life)[0]
        return newborns, adults, newborns + adults

result = rabbits(month, lifespan)

print(result[0], result[1], result[2])
w.write(str(result[2]))

f.close()
w.close()