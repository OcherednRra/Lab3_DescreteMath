import tkinter as tk

class StudentInfoWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.normal_font = ("Segoe UI", 9, 'normal')
        self.bold_font = ("Segoe UI", 9, 'bold')
        self.italic_font = ("Segoe UI", 9, 'italic')

        self.window_configuration()
        self.option_info()
        self.option_calculation()

    def window_configuration(self):
        self.geometry('350x184')
        self.title("Інформація")
        self['bg'] = 'grey'

    def option_info(self):
        info_frame = tk.Frame(self)
        info_frame.pack(fill=tk.BOTH, pady=(4, 6))

        student = {
            'Підготував': 'Поляков Валентин Олегович',
            'Група': "ІО-15",
            "Номер у списку групи": "15"
        }

        # first column (keys)
        for i, str_ in enumerate(student.keys()):
            tk.Label(info_frame, text=str_, font=self.bold_font).grid(column=0, row=i, sticky='w')

        # second column (values)
        for i, str_ in enumerate(student.values()):
            tk.Label(info_frame, text=str_).grid(column=1, row=i, sticky='w')

    def option_calculation(self):
        frame_variant = tk.Frame(self)
        frame_variant.pack(fill=tk.BOTH)

        option_number = f"{1515%10 + 1}"

        option = {
            "Розрахунок варіанту лабораторної роботи": self.bold_font,
            "Варіант лабораторної роботи обчислюється за формулою:": self.italic_font,
            "NZK % 10 + 1,": self.normal_font,
            "де NZK - номер залікової книжки": self.italic_font,
            "Тому номер варіанту = 1515%10 + 1 = "+option_number: self.bold_font,
        }

        for str_, f in option.items():
            tk.Label(frame_variant, text=str_, font=f).pack()
