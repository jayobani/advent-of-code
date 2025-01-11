from itertools import chain
from collections import defaultdict

dg = defaultdict(set)
ul = list()
with open("aoc_2024_05_input.txt") as file:
    ip = 0
    for l in file:
        if(l.rstrip() == ""):
            ip += 1
        elif(ip == 0):
            t = tuple(map(int, l.rstrip().split("|")))
            dg[t[1]].add(t[0])
        elif(ip == 1):
            ul.append(list(map(int, l.rstrip().split(","))))
    
result = 0
for u in ul:
    allEqual = True
    o = [0] * len(u)
    us = set(u)
    for n in us:
        i = len(us & dg[n])
        if(n != u[i]):
            allEqual = False
        o[i] = n
    if(not allEqual):
        result += o[len(u) // 2]
print(result)