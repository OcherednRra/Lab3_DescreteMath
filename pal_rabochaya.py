from tkinter import *
import random
import networkx as nx
import pylab as pl


class Lab3:

    def create_tabl_random(self, n):
        self.tabl = []
        for i in range(n):
            self.tabl.append([])
            for j in range(n):
                self.tabl[i].append(random.randint(1, 20))
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.tabl[i][j] = 0
                else:
                    self.tabl[i][j] = self.tabl[j][i]
        return self.tabl

    def Dijkstra(self, N, S, w, Last_Node):
        inf = float("inf")
        dist = [inf] * N
        dist[S-1] = 0
        prev = [None] * N
        used = [False] * N
        min_dist = 0
        min_vertex = S-1
        try:
            while min_dist < inf:
                i = min_vertex
                used[i] = True
                for j in range(N):
                    if w[i][j] == "0":
                        w[i][j] = inf
                        if dist[i] + float(w[i][j]) < dist[j]:
                            dist[j] = dist[i] + float(w[i][j])
                            prev[j] = i
                    else:
                        if dist[i] + float(w[i][j]) < dist[j]:
                            dist[j] = dist[i] + float(w[i][j])
                            prev[j] = i
                min_dist = inf
                for j in range(N):
                    if not used[j] and dist[j] < min_dist:
                        min_dist = dist[j]
                        min_vertex = j
            path = []
            j = Last_Node - 1
            while j is not None:
                path.append(j)
                j = prev[j]
            path = path[::-1]
            result = []
            for i in range(len(path)-1):
                result.append((path[i]+1,path[i+1]+1))

            pl.figure('Найкоротший шлях з вершини {} в вершину {}'.format(S, Last_Node))
            self.graph = nx.Graph()
            for i in range(N):
                self.graph.add_node(i+1)
            for i in range(len(w)):
                for j in range(len(w[i])):
                    if w[i][j] != inf:
                        self.graph.add_edge(i+1, j+1, weight=w[i][j])
            nx.draw_networkx(self.graph, pos=nx.shell_layout(self.graph), width=1, font_size=13)
            edge_labels = dict([((u, v,), d['weight']) for u, v, d in self.graph.edges(data=True)])
            nx.draw_networkx_edge_labels(self.graph, pos=nx.shell_layout(self.graph),
                                         edge_labels=edge_labels, label_pos=0.3, font_size=9)
            nx.draw_networkx_edges(self.graph, pos=nx.shell_layout(self.graph), edgelist=result, edge_color='lawngreen')
            pl.axis('off')
            pl.show()
        except:
            print("errorDijkstra")

    def student(self, nzk=6403):
        self.slave = Toplevel(self.root)
        self.slave.title('Student')
        self.slave.focus_set()
        self.slave.minsize(300, 100)
        self.slave.maxsize(300, 100)
        self.slave['bg'] = 'seashell'
        self.slave.wm_geometry("+600+250")
        Label(self.slave, text='Бровченко Анастасія\n'
                               'група ІО-64\n'
                               'варіант {}'.format(divmod(nzk, 10)[1]+1),
              justify=LEFT, font="Arial 17 bold", bg='seashell').pack(fill='both')

    def main_window(self):
        self.root = Tk()
        self.root.minsize(780, 350)
        self.root.maxsize(780, 350)
        self.root.title('Завдання (лабораторна №3)')

        def but_bind():
            if len(self.e.get()) == 0:
                Label(self.root, text='*задайте спершу кількість вершин графа', fg='red', font='Arial 12',)\
                    .grid(column=1, row=4, columnspan=2)
            else:
                self.window2()

        Label(self.root, text='Завдання', font='Arial 16 bold').grid(column=1, row=1)
        Label(self.root, text='1. Розглянути основні принципи пошуку найкоротших шляхів у графі. '
                              'Написати програму за алгоритмом Дейкстри для пошуку найкоротших шляхів у графі.'
                              '\n2. За правилом, наданим викладачем, сформувати матрицю ваг графа.'
                              '\n3. Представити граф, заданий матрицею ваг у графічній формі та виділити '
                              'найкоротший шлях між заданими викладачем вершинами, сформований за алгоритмом Дейкстри.',
              font='Arial 16', bg='ghostwhite', wraplength=800, justify=LEFT, padx=10).grid(column=1, row=2, columnspan=4)
        Label(self.root, text='Кількість вершин графа  ', font='Arial 14', pady=20, justify=RIGHT).grid(column=1, row=3, sticky=E)
        self.e = Entry(self.root, width=5, font='Arial 14')
        self.e.grid(column=2, row=3, sticky=W)
        Button(self.root, text='Задати матрицю ваг', font='Arial 12', bg='lightblue', command=but_bind). grid(column=3, row=3)
        Button(self.root, text='Студент', font='Arial 12 bold', command=self.student, bg='azure').grid(column=1, row=5)

        self.root.mainloop()

    def window2(self):
        self.slave2 = Toplevel(self.root)
        self.slave2.title('Задати матрицю ваг')
        self.slave2.focus_set()
        self.slave2.minsize(400, 400)

        def random_gen():
            tabl = self.create_tabl_random(int(self.e.get()))
            for i in range(int(self.e.get())):
                for j in range(int(self.e.get())):
                    self.list_ent[i][j].insert(END, tabl[i][j])

        for i in range(int(self.e.get())+1):
            for j in range(int(self.e.get())+1):
                if i == 0:
                    Label(self.slave2, text='{}'.format(j), font='Arial 16 bold', width=3).grid(column=j, row=i, sticky=W)
                elif j == 0:
                    Label(self.slave2, text='{}'.format(i), font='Arial 16 bold', width=3).grid(column=j, row=i, sticky=W)
                elif i == 0 and j == 0:
                    Label(self.slave2, text=' ', width=3).grid(column=j, row=i, sticky=W)
        self.list_ent = []
        for i in range(int(self.e.get())):
            self.list_ent. append([])
            for j in range(int(self.e.get())):
                self.list_ent[i].append(Entry(self.slave2, font='Arial 14', width=3))
                self.list_ent[i][j].grid(row=i+1, column=j+1, sticky=W)

        Label(self.slave2, text='   ').grid(column=2, columnspan=5, row=int(self.e.get())+1)
        Button(self.slave2, text='Згенерувати випадково', font='Arial 12', bg='mintcream', command=random_gen)\
            .grid(column=0, columnspan=5, row=int(self.e.get())+2)
        Button(self.slave2, text='Показати граф', font='Arial 12', bg='mintcream', width=15, command=self.show_gr)\
            .grid(column=5, row=int(self.e.get())+2, columnspan=5)

    def show_gr(self):
        self.tabl = []
        for i in range(int(self.e.get())):
            self.tabl.append([])
            for j in range(int(self.e.get())):
                self.tabl[i].append(self.list_ent[i][j].get())
        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                if self.tabl[i][i] != '0':
                    Label(self.slave2, text='*перевірте таблицю суміжності\n'
                                            'існує петля', font='Arial 12', fg='red')\
                        .grid(column=1, row=int(self.e.get())+3, columnspan=5)
                    pass

        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                self.list_ent[i][j]['state'] = DISABLED

        def button_bind():
            self.Dijkstra(N=int(self.e.get()), S=int(st.get()), Last_Node=int(en.get()), w=self.tabl)

        Label(self.slave2, text='Визначити найкоротший шлях між вершинами', wraplength=350, font='Arial 16 bold', pady=20)\
            .grid(column=1, row=int(self.e.get())+4, columnspan=10)
        Label(self.slave2, text='Початок:', font='Arial 14').grid(column=0, row=int(self.e.get())+5, columnspan=3)
        Label(self.slave2, text='Кінець:', font='Arial 14').grid(column=0, row=int(self.e.get())+6, columnspan=3)
        st = Entry(self.slave2, font='Arial 14', width=3)
        st.grid(column=3, row=int(self.e.get())+5, columnspan=2)
        en = Entry(self.slave2, font='Arial 14', width=3)
        en.grid(column=3, row=int(self.e.get())+6, columnspan=2)
        Button(self.slave2, text='Визначити', font='Arial 12 bold', command=button_bind, width=10)\
            .grid(column=5, row=int(self.e.get())+5, columnspan=3, rowspan=2)

        pl.figure('Заданий граф')

        self.gr = nx.Graph()
        for i in range(int(self.e.get())):
            self.gr.add_node(i+1, color='lawngreen')
        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                if self.tabl[i][j] != '0':
                    self.gr.add_edge(i+1, j+1, weight=self.tabl[i][j])
        edge_labels = nx.get_edge_attributes(self.gr, 'weight')
        pos = nx.circular_layout(self.gr)
        nx.draw_networkx(self.gr, pos)
        nx.draw_networkx_edge_labels(self.gr, pos, edge_labels=edge_labels, label_pos=0.3)
        pl.axis('off')
        pl.show()

a = Lab3()
a.main_window()
