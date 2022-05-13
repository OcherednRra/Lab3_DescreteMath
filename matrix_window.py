from tkinter import *
from math import inf

class MatrixWindow(Toplevel):
    def __init__(self, table, command):
        super().__init__()
        self.title("Матриця найкоротших шляхів")
        self.geometry("400x320")

        weight = len(table)

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

        entries_list = []
        for i in range(weight):
            entries_list.append([])
            for j in range(weight):
                entries_list[i].append(Entry(matrix, width=4))
                entries_list[i][j].insert(END, table[i][j])
                entries_list[i][j].grid(row=i+1, column=j+1)


        self.shortest_button = Button(self, text="Показати граф найкоротших шляхів", width=35, command=command)
        self.shortest_button.pack(pady=(30, 0))
