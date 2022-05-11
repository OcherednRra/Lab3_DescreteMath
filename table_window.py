from tkinter import *
import random
import networkx as nx
import pylab

from floyd_warshall_algorithm import algorithm

class TableWindow(Toplevel):

    def __init__(self, weight_value):
        super().__init__()

        self.title('Задати матрицю ваг')
        self.focus_set()
        self.minsize(400, 400)

        self.weight = int(weight_value.get())
        self.table_window()

    def create_random_table(self, n):
        weight = self.weight

        self.table = []
        for i in range(n):
            self.table.append([])
            for j in range(n):
                self.table[i].append(random.randint(1, 20))

        for i in range(n):
            for j in range(n):
                if i == j:
                    self.table[i][j] = 0
                else:
                    self.table[i][j] = self.table[j][i]

        for i in range(weight):
            for j in range(weight):
                self.entries_list[i][j].insert(END, self.table[i][j])

    def create_table(self):
        weight = self.weight

        self.table = []
        for i in range(weight):
            self.table.append([])
            for j in range(weight):
                self.table[i].append(self.entries_list[i][j].get())

        for i in range(weight):
            for j in range(weight):
                if self.table[i][i] != '0':
                    Label(self, text="Error", fg='red').grid(column=1, row=weight+3, columnspan=5)
                    pass

        for i in range(weight):
            for j in range(weight):
                self.entries_list[i][j]['state'] = DISABLED

        s = "Визначити найкоротший шлях між вершинам"
        Label(self, text=s, pady=20).grid(column=1, row=weight+4, columnspan=10)
        s = "Початок: "
        Label(self, text=s).grid(column=0, row=weight+5, columnspan=3)
        s = "Кінець: "
        Label(self, text=s).grid(column=0, row=weight+6, columnspan=3)

        self.start_entry = Entry(self, width=3)
        self.start_entry.grid(column=3, row=weight+5, columnspan=2)

        self.end_entry = Entry(self, width=3)
        self.end_entry.grid(column=3, row=weight+6, columnspan=2)

        Button(self, text='Визначити', command=self.run_algorithm, width=10)\
            .grid(column=5, row=weight+5, columnspan=3, rowspan=2)

        pylab.figure('Заданий граф')
        graph = nx.Graph()

        for i in range(weight):
            graph.add_node(i+1, color='lawngreen')

        for i in range(weight):
            for j in range(weight):
                if self.table[i][j] != '0':
                    graph.add_edge(i+1, j+1, weight=self.table[i][j])

        edge_labels = nx.get_edge_attributes(graph, 'weight')
        pos = nx.circular_layout(graph)
        nx.draw_networkx(graph, pos)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, label_pos=0.3)

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

        Button(self, text='Random 🎲', command=lambda: self.create_random_table(weight))\
            .grid(column=0, columnspan=5, row=weight+2)
        Button(self, text='Показати граф', width=15, command=self.create_table)\
            .grid(column=5, row=weight+2, columnspan=5)

    def run_algorithm(self):
        algorithm(self, self.weight, int(self.start_entry.get()), int(self.end_entry.get()), self.table)
