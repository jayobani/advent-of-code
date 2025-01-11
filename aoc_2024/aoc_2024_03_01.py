from re import findall

il = list()
with open("aoc_2024_03_input.txt") as f:
    for l in f:
        il.append(l)

result = 0
pattern = "mul\([0-9]{1,3},[0-9]{1,3}\)"
for i in il:
    ml = findall(pattern, i)
    for m in ml:
        ci = m.find(",")
        result += int(m[4:ci]) * int(m[ci+1:-1])
print(result)
