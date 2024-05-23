import customtkinter as ctk
from Frame import Frame
from typing import Union
from sheet_class import Sheet_Obj
from tksheet import *

class FloatSpinbox(ctk.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: int = 1,
                 command: callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color
        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = ctk.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = ctk.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[int, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(float(value)))
def __create_sheet(self,frame):
        pass

class your_load(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry('800x500')
        self.title("Ручной ввод")
        self.attributes('-topmost', 1)
        self.data = [] #empty default data (Sheet data)
        self.configure(fg_color = 'RoyalBlue')
        settings_frame = table_frame = Frame(self, height = self.winfo_height(), width = 150,fg_color = 'white')
        settings_frame.grid(row=0,column=0,pady=6, padx=20)
        spinbox_col = FloatSpinbox(settings_frame, width=150, step_size=1)
        spinbox_row = FloatSpinbox(settings_frame, width=150, step_size=1)
        col_label = ctk.CTkLabel(settings_frame,text="Количество столбцов",font=("Arial",13))
        row_label = ctk.CTkLabel(settings_frame,text="Количество строк",font=("Arial",13))
        table_frame = Frame(self, height = 480, width = 560,fg_color = 'white')

        #------------------------create_sheet--------------------------------------#
        def callback_create_btn():
            self.data = [[0 for j in range(spinbox_col.get())] for i in range(spinbox_row.get())] #init size data

           # self.show.grid(row = 1, column = 0, sticky = "nswe")
            sheet_init_data = Sheet_Obj(table_frame, data=self.data,
                                         width=table_frame.winfo_width(), height=table_frame.winfo_height())
            
            sheet_init_data.grid(row = 0, column = 0, sticky = "nswe")
        #------------------------create_sheet--------------------------------------#

        #------------------------clean_sheet--------------------------------------#
        def clear_sheet(frame):
            frame.clean()
        #------------------------clean_sheet--------------------------------------#
        



        

        create_btn = ctk.CTkButton(settings_frame,text="Создать таблицу",font=("Arial",13),command=lambda:callback_create_btn())
        claer_btn = ctk.CTkButton(settings_frame,text="Очистить таблицу",font=("Arial",13),command=lambda:clear_sheet(table_frame))
        load_btn = ctk.CTkButton(settings_frame,text="Загрузить таблицу",font=("Arial",13),command=lambda:print('hello'))

        #-------------------------GRID_WIDGETS---------------------------------#
        col_label.grid(row=0, column=0, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        spinbox_col.grid(row=1, column=0, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        row_label.grid(row=2, column=0, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        spinbox_row.grid(row=3, column=0, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        create_btn.grid(row=4, column=0, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        claer_btn.grid(row=5, column=0, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        load_btn.grid(row=6, column=0, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        table_frame.grid(row=0,column=1,pady=6, padx=20)
        #-------------------------GRID_WIDGETS---------------------------------#



        #-----------------------------MAKE_WINDOW_MODAL----------------------------------#
        self.resizable(width=False, height=False)
        self.grab_set()
        self.focus_set()
        self.wait_window()
        
        #-----------------------------MAKE_WINDOW_MODAL----------------------------------#

