from tkinter import *
from tkinter import messagebox
import random
import networkx as nwx, matplotlib.pyplot as plt

dimension = 6
def get_dimension(event):
    top = Toplevel(height=500, width=500, relief=GROOVE)
    ent = Entry(top, width=50, bd=3)
    ent.grid(row=1, column=1, sticky=W + E + N + S, pady=5, padx=5)
    def sets(event):
        global dimension
        dimension = int(ent.get())

    but1 = Button(top, text='OK!', font='arial 20')
    but1.grid(row=2, column=1, sticky=W + E + N + S, pady=5, padx=5)
    but1.bind("<Button-1>", sets)


def created_matrix(event):
    top = Toplevel(height=500, width=500, relief = GROOVE)
    #top.maxsize(width=300,height=75)
    #top.minsize(width=300,height=75)
    top.title("Created matrix")


    def save_edges(event):
        global edges
        edges = list(listbox2.get(0,END))

    allEdges = []
    for i in range(dimension):
        for j in range(dimension):
            appended = (i,j)
            allEdges.append(appended)
    for i in allEdges:
        if (i[1],i[0]) in allEdges:
            allEdges.remove(i)

    listbox1 = Listbox(top, height=27, width=4, font=("Arial", 16), selectmode=EXTENDED)

    for i in allEdges:
        listbox1.insert(END, i)

    listbox1.grid(row=1, column=1, sticky=W + E + N + S, pady=5, padx=5)

    listbox2 = Listbox(top, height=27, width=4, font=("Arial", 16), selectmode=EXTENDED)
    listbox2.grid(row=1, column=2, sticky=W + E + N + S, pady=5, padx=5)

    def callback(event):
        value = listbox1.get(ACTIVE)
        listbox1.delete(ACTIVE)
        listbox2.insert(END, value)

    but1 = Button(top, text='Set dimention', font='arial 20')
    but1.bind("<Button-1>", callback)
    but1.grid(row=2, column=1, columnspan=2, sticky=W + E + N + S, pady=5, padx=5)

    but2 = Button(top, text='Save edges', font='arial 20')
    but2.bind("<Button-1>", save_edges)
    but2.grid(row=3, column=1, columnspan=2, sticky=W + E + N + S, pady=5, padx=5)


def created_graph(event):
    graf1 = nwx.Graph()
    for i in edges:
        graf1.add_nodes_from(i)
    for i, j in edges:
        graf1.add_edge(i, j)
    nwx.draw(graf1, pos=nwx.shell_layout(graf1), alpha=0.6, edge_color='b', font_size=20,
             node_size=700, arrows=True, with_labels=True)
    plt.show()


