
with open("aoc_2024_02_input.txt") as f:
    rl = list()
    for l in f:
        rl.append(list(map(int, l.split())))

result = 0
for r in rl:
    increasing = (r[1] > r[0])
    for ri in range(1, len(r)):
        if(r[ri-1] < r[ri] and increasing and 1 <= (r[ri] - r[ri-1]) <= 3):
            continue
        elif(r[ri-1] > r[ri] and not increasing and 1 <= (r[ri-1] - r[ri]) <= 3):
            continue
        else:
            break
    else:
        result += 1
print(result)
