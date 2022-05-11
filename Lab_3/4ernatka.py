def graph_input():
    N = int(input("Количество вершин в грaфе: "))
    weight = [[float("+inf")] * N for j in range(N)]
    for i in range(N):
        weight[i][i] = 0
    M = int(input("Количество рёбер в грaфе: "))
    for i in range(M):
        a, b, w = input().split()
        a, b, w = int(a), int(b), int(w)
        weight[a][b] = w
        weight[b][a] = w
    return weight


def print_matrix(A):

  print(A)


from  copy import deepcopy

def floyd(weight):
    N = len(weight)
    F = deepcopy(weight)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                F[i][j] = min(F[i][j], F[i][k] + F[k][j])

    return F

G = graph_input()
print_matrix(G)
F = floyd(G)
print_matrix(F)
