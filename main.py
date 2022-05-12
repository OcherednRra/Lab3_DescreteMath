from tkinter import *

from student_info_window import StudentInfoWindow
from table_window import TableWindow


class Lab3(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x150')
        self.resizable(width=False, height=False)
        self.title('Лабораторна робота №3')

        self.main_window()

    def main_window(self):

        self.about_student_button()

        Label(self, text="Кількість вершин графа: ", justify=LEFT).grid(column=0, row=1, pady=(20, 0), padx=(10, 0), sticky=E)
        self.e = Entry(self)
        self.e.grid(column=1, row=1, sticky="e", pady=(20, 0))
        Button(self, text='Задати матрицю ваг', command=self.open_table_window).grid(column=0, columnspan=2, row=3, pady=(30, 0), padx=(30, 0))

    def about_student_button(self):
        Button(self, width=16, height=1, fg='#d9073d', relief="raised", font=("Segoe UI", 11, 'bold'),
                  text='!  Інфо  !', activebackground='grey',
                  command=self.open_student_info_window).grid(column=0, row=0, padx=(30, 0), columnspan=2, pady=(10, 0))
    
    def open_student_info_window(self):
        student_info_window = StudentInfoWindow(self)
        student_info_window.grab_set()

    def open_table_window(self):
        table_window = TableWindow(self.e)
        table_window.grab_set()


if __name__ == "__main__":
    app = Lab3()
    app.mainloop()
