from tkinter import *

from student_info_window import StudentInfoWindow
from table_window import TableWindow


class Lab3(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('780x350')
        self.resizable(width=False, height=False)
        self.title('Лабораторна робота №3')

        self.main_window()

    def main_window(self):

        def but_bind():
            if len(self.e.get()) == 0:
                Label(self, text='*задайте спершу кількість вершин графа', fg='red', font='Arial 12',)\
                    .grid(column=1, row=4, columnspan=2)
            else:
                self.open_table_window()

        self.about_student_button()

        Label(self, text='Кількість вершин графа  ', font='Arial 14', pady=20, justify=RIGHT).grid(column=1, row=3, sticky=E)
        self.e = Entry(self, width=5, font='Arial 14')
        self.e.grid(column=2, row=3, sticky=W)
        Button(self, text='Задати матрицю ваг', font='Arial 12', bg='lightblue', command=but_bind). grid(column=3, row=3)

    def about_student_button(self):
        Button(self, width=18, height=1, fg='#d9073d', relief="raised",
                  text='!  Інформація  !', activebackground='grey',
                  command=self.open_student_info_window).grid(pady=(10, 20))

    def open_student_info_window(self):
        student_info_window = StudentInfoWindow(self)
        student_info_window.grab_set()

    def open_table_window(self):
        table_window = TableWindow(self.e)
        table_window.grab_set()


if __name__ == "__main__":
    app = Lab3()
    app.mainloop()
