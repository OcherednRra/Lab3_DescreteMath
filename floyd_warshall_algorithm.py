import math
import pylab
import networkx as nx

def algorithm(self, weight, start, end, table):
    inf = math.inf
    dist = [inf] * weight
    dist[start-1] = 0
    previous = [None] * weight
    used = [False] * weight
    min_dist = 0
    min_vertex = start-1

    # Алгоритм Флойда-Уоршилда
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

    # Візуалізація найкоротшого шляху
    pylab.figure(f"Найкоротший шлях з вершини {start} в вершину {end}")

    graph = nx.Graph()
    for i in range(weight):
        graph.add_node(i+1)

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != inf:
                graph.add_edge(i+1, j+1, weight=table[i][j])

    edge_labels = dict([((u, v,), d['weight']) for u, v, d in graph.edges(data=True)])

    nx.draw_networkx(graph, pos=nx.shell_layout(graph), width=1, font_size=13)
    nx.draw_networkx_edge_labels(graph, pos=nx.shell_layout(graph), edge_labels=edge_labels, label_pos=0.3, font_size=9)
    nx.draw_networkx_edges(graph, pos=nx.shell_layout(graph), edgelist=result, edge_color='lawngreen')

    pylab.axis('off')
    pylab.show()
