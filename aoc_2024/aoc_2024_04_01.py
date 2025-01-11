from collections import deque
g = list()
bfs = deque()
nl = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if((i, j) != (0, 0))]

with open("aoc_2024_04_input.txt") as f:
    for l in f:
        g.append(list(l.rstrip()))
        for gi in range(len(g[-1])):
            if(g[-1][gi] == "X"):
                vt = (len(g)-1, gi)
                for nt in nl:
                    bfs.append(((len(g)-1, gi), nt))

n, m = len(g), len(g[0])
for a in ["M", "A", "S"]:
    len_bfs = len(bfs)
    for i in range(len_bfs):
        vt, nt = bfs.popleft()
        ut = (vt[0] + nt[0], vt[1] + nt[1])
        if(0 <= ut[0] < n and 0 <= ut[1] < m and g[ut[0]][ut[1]] == a):
            bfs.append((ut, nt))

result = len(bfs)
print(result)

