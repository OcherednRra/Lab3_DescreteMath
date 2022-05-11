import Create_matrix
from copy import deepcopy
from tkinter import *

def floyd(event):


    top = Toplevel(height=500, width=50, relief=GROOVE)
    top.title("Matrix")

    K = len(Create_matrix.weight)
    F = deepcopy(Create_matrix.weight)
    for k in range(K):
        for i in range(K):
            for j in range(K):
                F[i][j] = min(F[i][j], F[i][k] + F[k][j])

    lab4 = Label(top, text='N', font='arial 20')
    lab4.grid(row=0, column=0)


    for i in range(len(F)):
        lab1 = Label(top, text=i, font='arial 20')
        lab2 = Label(top, text=i, font='arial 20')
        lab1.grid(row=i + 1, column=0)
        lab2.grid(row=0, column=i + 1)
    for i in range(len(F)):
        f = 1
        for j in F[i]:
            lab1 = Label(top, text=j, font='arial 20')
            lab1.grid(row=i+1, column=f)
            f += 1

