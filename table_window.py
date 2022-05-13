from tkinter import *
import random
import networkx as nx
import pylab
from math import inf

from matrix_window import MatrixWindow
from floyd_warshall_algorithm import algorithm

class TableWindow(Toplevel):

    def __init__(self, weight_value):
        super().__init__()

        self.title("Матриця ваг")
        self.geometry("400x320")

        self.weight = int(weight_value.get())
        self.window()

    def create_weitghing_matrix(self):
        weight = self.weight

        """ Формирование весовой матрицы """
        table = []
        for i in range(weight):
            table.append([])
            for j in range(weight):
                table[i].append(self.entries_list[i][j].get())

        # приведение к int/inf
        for i in range(weight):
            for j in range(weight):
                if table[i][j] == "" or table[i][j] == "0":
                    table[i][j] = inf
                    continue
            for j in range(weight):
                if table[i][j] != inf:
                    table[i][j] = int(table[i][j])

        self.table = table


    def shortest_paths_matrix(self):
        """ Матрица кратчайших путей (алгоритм Флойда-Уоршилда) """
        self.table = algorithm(self.table)

    def show_table(self):
        self.create_weitghing_matrix()
        # відключення функції
        self.create_weitghing_matrix = lambda: None

        weight = self.weight
        table = self.table

        # Візуалізація найкоротшого шляху
        pylab.figure("Візуалізація матриці")

        graph = nx.Graph()
        for i in range(weight):
            graph.add_node(i+1)

        for i in range(len(table)):
            for j in range(len(table[i])):
                if i == j:
                    continue

                if table[i][j] != inf:
                    graph.add_edge(i+1, j+1, weight=table[i][j])

        edge_labels = dict([((u, v,), d["weight"]) for u, v, d in graph.edges(data=True)])

        nx.draw_networkx(graph, pos=nx.shell_layout(graph), width=1, font_size=13)
        nx.draw_networkx_edge_labels(graph, pos=nx.shell_layout(graph), edge_labels=edge_labels, label_pos=0.3, font_size=9)

        pylab.axis("off")
        pylab.show()

    def window(self):
        weight = self.weight

        master = Frame(self)
        master.pack(pady=(10, 0))

        matrix = Frame(master)
        matrix.grid(row=0)

        for i in range(weight + 1):
            for j in range(weight + 1):
                grids = {"column": j, "row": i, "sticky": W+E+N+S}
                if i == 0:
                    Label(matrix, text=j).grid(**grids)
                elif j == 0:
                    Label(matrix, text=i).grid(**grids)

        self.entries_list = []
        for i in range(weight):
            self.entries_list.append([])
            for j in range(weight):
                self.entries_list[i].append(Entry(matrix, width=4))
                self.entries_list[i][j].grid(row=i+1, column=j+1)

        Button(master, text="Показати граф, заданий матрицею", width=35, command=self.show_table)\
            .grid(row=weight+4, pady=(30, 0))

        Button(master, text="Показати матрицю найкоротших шляхів", width=35, command=self.open_matrix_window)\
            .grid(row=weight+5)

    def open_matrix_window(self):
        self.shortest_paths_matrix()
        matrix_window = MatrixWindow(self.table, self.show_table)
        matrix_window.grab_set()
