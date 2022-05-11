from tkinter import *

def create_window_2(event):
    #Create Toplevel for window 2
    window2 = Toplevel()
    window2.title("Window 2")
    #window2.maxsize(width=475,height=290)
    #window2.minsize(width=475,height=290)



    def get_node(event):
        global N
        N = int(ent1.get())


    def get_edge(event):
        global M
        M = int(ent2.get())

    def get_matrix(event):
        global weight
        weight2 = []
        global value
        value = []
        weight = [[float("+inf")] * N for j in range(N)]
        for i in range(N):
            weight[i][i] = 0
        for i in range(M):
            step = tex1.get(float(i + 1), float(i + 2)).rstrip("\n")
            weight2.append(step)
        for i in weight2:
            apee = i.split()
            value.append(apee)
        for i in range(len(value)):
            for j in range(len(value[i])):
                value[i][j] = int(value[i][j])
        for i in value:
            weight[i[0]][i[1]] = i[2]
            weight[i[1]][i[0]] = i[2]



    lab1 = Label(window2, text='Nodes', font='arial 20')
    lab2 = Label(window2, text='Edges', font='arial 20')
    lab3 = Label(window2, text='Matrix', font='arial 20')



    ent1 = Entry(window2, width=50, bd=3)
    ent2 = Entry(window2, width=50, bd=3)
    tex1 = Text(window2, width=10, height=20, font="Verdana 12", wrap=WORD)

    but1 = Button(window2, text='Set nodes', font='arial 20')
    but1.bind("<Button-1>", get_node)
    but2 = Button(window2, text='Set edges', font='arial 20')
    but2.bind("<Button-1>", get_edge)
    but3 = Button(window2, text='Set matrix', font='arial 20')
    but3.bind("<Button-1>", get_matrix)

    lab1.grid(row=1, column=1, sticky=W + E + N + S, pady=5, padx=5)
    lab2.grid(row=1, column=2, sticky=W + E + N + S, pady=5, padx=5)
    lab3.grid(row=4, column=1, columnspan=2, sticky=W + E + N + S, pady=5, padx=5)

    ent1.grid(row=2, column=1, sticky=W + E + N + S, pady=5, padx=5)
    ent2.grid(row=2, column=2, sticky=W + E + N + S, pady=5, padx=5)
    tex1.grid(row=5, column=1, columnspan=2,  sticky=W + E + N + S, pady=5, padx=5)

    but1.grid(row=3, column=1, sticky=W + E + N + S, pady=5, padx=5)
    but2.grid(row=3, column=2, sticky=W + E + N + S, pady=5, padx=5)
    but3.grid(row=6, column=1, columnspan=2, sticky=W + E + N + S, pady=5, padx=5)



'''
def graph_input(event):
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
    return  weight
'''
