g = list()
with open("aoc_2024_04_input.txt") as f:
    for l in f:
        g.append(list(l.rstrip()))
n, m = len(g), len(g[0])

result = 0
nl = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if(i in (1, -1) and j in (1, -1))]
for r in range(1, n-1):
    for c in range(1, m-1):
        if(g[r][c] == "A"):
            masCnt = 0
            for ni in range(len(nl)):
                if((g[r+nl[ni][0]][c + nl[ni][1]], g[r+nl[len(nl)-ni-1][0]][c + nl[len(nl)-ni-1][1]]) == ("M","S")):
                    masCnt += 1
            if(masCnt == 2):
                result += 1
print(result)

