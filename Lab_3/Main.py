from tkinter import *
from tkinter import messagebox
import Create_matrix
import Create_graph
import floyd

root = Tk()
root.title("Main Window")

#root.maxsize(width=320, height=190)
#root.minsize(width=320, height=190)


# My uniq task
NZK = 6305
number = NZK % 10 + 1
task = "Personal task number - " + str(number)


# #####################MAINLOOOOOOOP################

# Info about student
lab1 = Label(root, text='Create by Andrew Bratun', font='arial 20')
lab2 = Label(root, text='My number NZK - 6305', font='arial 20')
lab4 = Label(root, text=task, font='arial 20')
but1 = Button(root, text='Set the matrix of weights', font='arial 20')
but1.bind("<Button-1>", Create_matrix.create_window_2)
but2 = Button(root, text='See the graph', font='arial 20')
but2.bind("<Button-1>", Create_graph.created_graph)
but3 = Button(root, text='Shortest ways', font='arial 20')
but3.bind("<Button-1>", floyd.floyd)

# Info about student
lab1.grid(row=1, column=1, sticky=W+E+N+S, pady=5, padx=5)
lab2.grid(row=2, column=1, sticky=W+E+N+S, pady=5, padx=5)
lab4.grid(row=3, column=1, sticky=W+E+N+S, pady=5, padx=5)

but1.grid(row=4, column=1, sticky=W+E+N+S, pady=5, padx=5)
but2.grid(row=5, column=1, sticky=W+E+N+S, pady=5, padx=5)
but3.grid(row=6, column=1, sticky=W+E+N+S, pady=5, padx=5)

# Menu
m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label="Windows", menu=fm)
fm.add_command(label="Window№2", )
fm.add_command(label="Window№3", )
fm.add_command(label="Window№4", )


'''def exitwindow():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", exitwindow)
'''

# Xz
root.mainloop()
