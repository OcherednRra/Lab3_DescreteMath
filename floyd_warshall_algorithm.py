import pylab
import networkx as nx
from math import inf

def algorithm(table):
    N = len(table)                                      # число вершин в графе
    P = [[v for v in range(N)] for u in range(N)]       # начальный список предыдущих вершин для поиска кратчайших маршрутов

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d = table[i][k] + table[k][j]
                if table[i][j] > d:
                    table[i][j] = d
                    P[i][j] = k     # номер промежуточной вершины при движении от i к j

    # нумерацця вершин начинается с нуля
    for start in range(N):
        for end in range(N):
            if start <= end:
                path = [end+1]
                while end != start:
                    end = P[end][start]
                    path.append(end+1)

                frst = path[0]-1
                lst = path[-1]-1

                epath = []
                for k in range(len(path)):
                    if path[k] == path[-1]:
                        break
                    epath.append((path[k], path[k+1]))

                path = epath

                s = 0
                for (n, m) in path:
                    s += table[n-1][m-1]

                if table[frst][lst] != inf:
                    table[frst][lst] = s
                    table[lst][frst] = s

    return table
