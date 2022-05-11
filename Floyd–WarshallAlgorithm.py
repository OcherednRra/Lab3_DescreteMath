import math


def get_path(previous, u, v):
    path = [u]
    while u != v:
        u = previous[u][v]
        path.append(u)

    return path


table = [[       0,        2, math.inf,        3,        1, math.inf, math.inf,       10],
     [       2,        0,        4, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf,        4,        0, math.inf, math.inf, math.inf, math.inf,        3],
     [       3, math.inf, math.inf,        0, math.inf, math.inf, math.inf,        8],
     [       1, math.inf, math.inf, math.inf,        0,        2, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf,        2,        0,        3, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf,        3,        0,        1],
     [      10, math.inf,        3,        8, math.inf, math.inf,        1,        0],]

weight = len(table)                       # число вершин в графе
previous = [[v for v in range(weight)] for u in range(weight)]       # начальный список предыдущих вершин для поиска кратчайших маршрутов

for k in range(weight):
    for i in range(weight):
        for j in range(weight):
            d = table[i][k] + table[k][j]
            if table[i][j] > d:
                table[i][j] = d
                previous[i][j] = k     # номер промежуточной вершины при движении от i к j

# нумерацця вершин начинается с нуля
start = 1
end = 4
result = get_path(previous, end, start)
print(result)

def Dijkstra(self, weight, start, end, table):

    inf = math.inf
    dist = [inf] * weight
    dist[start-1] = 0
    previous = [None] * weight
    used = [False] * weight
    min_dist = 0
    min_vertex = start-1

    # Алгоритм Флойда-Уоршилда
    try:
        while min_dist < inf:
            i = min_vertex
            used[i] = True

            for j in range(weight):
                if table[i][j] == "0":
                    table[i][j] = inf

                if dist[i] + float(table[i][j]) < dist[j]:
                    dist[j] = dist[i] + float(table[i][j])
                    previous[j] = i

            min_dist = inf
            for j in range(weight):
                if not used[j] and dist[j] < min_dist:
                    min_dist = dist[j]
                    min_vertex = j

        path = []
        j = end - 1

        while j is not None:
            path.append(j)
            j = previous[j]

        path = path[::-1]
        result = []
        for i in range(len(path)-1):
            result.append((path[i]+1,path[i+1]+1))

        print(result)

        # Візуалізація найкоротшого шляху
        pylab.figure(f"Найкоротший шлях з вершини {start} в вершину {end}")

        self.graph = nx.Graph()
        for i in range(weight):
            self.graph.add_node(i+1)

        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] != inf:
                    self.graph.add_edge(i+1, j+1, weight=table[i][j])

        edge_labels = dict([((u, v,), d['weight']) for u, v, d in self.graph.edges(data=True)])

        nx.draw_networkx(self.graph, pos=nx.shell_layout(self.graph), width=1, font_size=13)
        nx.draw_networkx_edge_labels(self.graph, pos=nx.shell_layout(self.graph), edge_labels=edge_labels, label_pos=0.3, font_size=9)
        nx.draw_networkx_edges(self.graph, pos=nx.shell_layout(self.graph), edgelist=result, edge_color='lawngreen')

        pylab.axis('off')
        pylab.show()
    except:
        print("AlgorithmError")
