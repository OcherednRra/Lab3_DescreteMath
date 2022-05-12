from tkinter import *
import random
import networkx as nx
import pylab
import math

from floyd_warshall_algorithm import algorithm

class TableWindow(Toplevel):

    def __init__(self, weight_value):
        super().__init__()

        self.title('Задати матрицю ваг')
        self.focus_set()
        self.minsize(400, 400)

        self.weight = int(weight_value.get())
        self.table_window()

    def create_table(self):
        weight = self.weight

        table = []
        for i in range(weight):
            table.append([])
            for j in range(weight):
                table[i].append(self.entries_list[i][j].get())

        for i in range(weight):
            for j in range(weight):
                if table[i][i] != '0':
                    Label(self, text="Error", fg='red').grid(column=1, row=weight+3, columnspan=10)
                    pass

        inf = math.inf
        dist = [inf] * weight
        dist[0] = 0
        previous = [None] * weight
        used = [False] * weight
        min_dist = 0
        min_vertex = 1-1

        # Алгоритм Флойда-Уоршилда
        while min_dist < inf:
            i = min_vertex
            used[i] = True

            for j in range(weight):
                if table[i][j] == "":
                    table[i][j] = inf

                if table[i][j] == "0":
                    table[i][j] = 0

                if dist[i] + float(table[i][j]) < dist[j]:
                    dist[j] = dist[i] + float(table[i][j])
                    previous[j] = i

            min_dist = inf
            for j in range(weight):
                if not used[j] and dist[j] < min_dist:
                    min_dist = dist[j]
                    min_vertex = j

        print(table)
        path = []
        j = 7 - 1

        while j is not None:
            path.append(j)
            j = previous[j]

        print(path)
        path = path[::-1]
        result = []
        for i in range(len(path)-1):
            result.append((path[i]+1,path[i+1]+1))

        print(path)
        print(result)
        # Візуалізація найкоротшого шляху
        pylab.figure(f"Найкоротший шлях")

        graph = nx.Graph()
        for i in range(weight):
            graph.add_node(i+1)

        for i in range(len(table)):
            for j in range(len(table[i])):
                if i == j:
                    continue

                if table[i][j] != inf:
                    graph.add_edge(i+1, j+1, weight=table[i][j])

        edge_labels = dict([((u, v,), d['weight']) for u, v, d in graph.edges(data=True)])

        nx.draw_networkx(graph, pos=nx.shell_layout(graph), width=1, font_size=13)
        nx.draw_networkx_edge_labels(graph, pos=nx.shell_layout(graph), edge_labels=edge_labels, label_pos=0.3, font_size=9)
        nx.draw_networkx_edges(graph, pos=nx.shell_layout(graph), edgelist=result, edge_color='lawngreen')

        pylab.axis('off')
        pylab.show()

    def table_window(self):
        weight = self.weight

        for i in range(weight + 1):
            for j in range(weight + 1):
                grids = {"column": j, "row": i, "sticky": W}
                if i == 0:
                    Label(self, text='{}'.format(j)).grid(**grids)
                elif j == 0:
                    Label(self, text='{}'.format(i)).grid(**grids)
                elif i == 0 and j == 0:
                    Label(self, text=' ').grid(**grids)

        self.entries_list = []
        for i in range(weight):
            self.entries_list.append([])
            for j in range(weight):
                self.entries_list[i].append(Entry(self, width=4))
                self.entries_list[i][j].grid(row=i+1, column=j+1, sticky=W)

        #Button(self, text="🎲", font=("Segoe UI", 18), height=1, width=5, command=lambda: self.create_random_table(weight))\
        #    .grid(column=0, columnspan=5, row=weight+2, pady=(10, 0))
        Button(self, text='Показати граф', width=15, command=lambda: self.create_table())\
            .grid(column=5, row=weight+2, columnspan=5)

    def run_algorithm(self):
        algorithm(self, self.weight, int(1), int(7), self.table)
