with open("aoc_2024_02_input.txt") as f:
    rl = list()
    for l in f:
        rl.append(list(map(int, l.split())))

result = 0
for r in rl:
    for ri in range(len(r)):
        i = (1 if(ri == 0) else 0)
        j = (2 if(ri <= 1) else 1)
        increasing = r[i] < r[j]
        for rj in range(len(r)-2):
            if(r[i] < r[j] and increasing and 1 <= (r[j] - r[i]) <= 3):
                i += 1 + ((i+1) == ri)
                j += 1 + ((j+1) == ri)
                continue
            elif(r[i] > r[j] and not increasing and 1 <= (r[i] - r[j]) <= 3):
                i += 1 + ((i+1) == ri)
                j += 1 + ((j+1) == ri)
                continue
            else:
                break            
        else:
            result += 1
            break
print(result)

