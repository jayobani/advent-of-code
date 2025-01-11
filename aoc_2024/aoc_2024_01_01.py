al = list()
bl = list()
with open("aoc_2024_01_input.txt") as f:
    for l in f:
        a, b = map(int, l.split())
        al.append(a)
        bl.append(b)
result = sum(abs(t[0] - t[1]) for t in zip(sorted(al), sorted(bl)))
print(result)
