from collections import Counter

al = list()
bl = list()
with open("aoc_2024_01_input.txt") as f:
    for l in f:
        a, b = map(int, l.split())
        al.append(a)
        bl.append(b)

bc = Counter(bl)
result = 0
for k in al:
    if k in bc:
        result += (k  * bc[k])
print(result)
