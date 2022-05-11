from tkinter import *
import networkx as nwx, matplotlib.pyplot as plt
import Create_matrix


def created_graph(event):
    graf1 = nwx.Graph()
    edges = []
    for i in Create_matrix.value:
        edges.append(i[:2])
    for i in edges:
        graf1.add_nodes_from(i)
    for i in edges:
        graf1.add_edges_from(edges)
    nwx.draw(graf1, pos=nwx.shell_layout(graf1), alpha=0.6, edge_color='b', font_size=20,
             node_size=700, arrows=True, with_labels=True)
    plt.show()
