#####################################################################
# Данный класс реализует таблицу с возможностью заполнения:
# 1) вручную
# 2) из excel 
# 3) из базы данных SQLite
# Оборачивает таблицу в Frame для более удобного расположения на окне
##################################################################### 
import customtkinter as ctk
from tksheet import *
#import pandas as pd
#from scipy.stats import kurtosis, skew
#import calculate_functions as calcus 
import Frame
  

# ROW_COUNT = 22
# COL_COUNT = 9
# STAT_ROW_COUNT = 8
# NAME_FILE = r"C:\Users\Admin\Desktop\matrix.XLSX"
       
# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         #self.geometry("600x400")
#         self.title("Statistic")
#         self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

# app = App()
# fr = Frame.MyFrame(master = app, width = 700, height = 500)
# row_data = pd.read_excel(NAME_FILE, engine = "openpyxl",header = None)
# data = pd.read_excel(NAME_FILE, engine = "openpyxl",header = None).values.tolist()

# tb_data = Sheet(fr, data=data, width=500, height=600)
# tb_data.enable_bindings()
# tb_data.grid_columnconfigure(0, weight=1)
# tb_data.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)
# fr_statistic = Frame.MyFrame(master = app, width = 700, height = 500)
# fr_statistic.place(x=800,y=20)



# data_stat = [["" for i in range(COL_COUNT)] for j in range(STAT_ROW_COUNT)]

# HEAD_COL = ["Параметры","Мода", "Медиана", "Дисперсия","Cр. арифм.", "Эксцесс",
#             "Коэф. ассиметрии","Мат.Ожидание"]

# HEAD_ROW = ["Средняя стоимость м2 жилья (рублей)", "Размер ставки по ипотеке (%)",
#         "Средняя зарплата ( рублей)", "Уровень инфляции (%)", "Количество м2 жилья на душу населения (м2/чел.)",
#         "Количество м2 жилья, введенного в эксплуатацию (млн,м2)","Количество семей, улучшивших жилищное положение (чел.)",
#         "Средняя стоимость строительства (руб.)",""] 

# for i in range(0, STAT_ROW_COUNT):
#     data_stat[i][0] = HEAD_COL[i]

# for i in range(1, COL_COUNT):
#     data_stat[0][i] = HEAD_ROW[i-1]

# def average(lst):
#     return sum(lst)/float(len(lst))

# sr_stoimost = calcus.get_column_data(row_data,1)
# ipoteka = calcus.get_column_data(row_data,2)
# zp = calcus.get_column_data(row_data,3)
# inflation = calcus.get_column_data(row_data,4)
# heart_metres = calcus.get_column_data(row_data,5)
# builded_metres = calcus.get_column_data(row_data,6)
# famalies = calcus.get_column_data(row_data,7)
# stoimost_stroy = calcus.get_column_data(row_data,8)
# lst = [sr_stoimost,ipoteka,zp,inflation,heart_metres,builded_metres,famalies,stoimost_stroy]
# func_lst = [statistics.mode, statistics.median, statistics.pvariance, average,kurtosis,skew,statistics.mean]

# cnt = 1
# for func in func_lst:
#     for i in range(1, COL_COUNT):
#         data_stat[cnt][i] = func(lst[i-1])
#     cnt=cnt+1



# tb_statistic = Sheet(fr_statistic, data=data_stat, width=500, height=600)
# tb_statistic.enable_bindings()
# tb_statistic.grid_columnconfigure(0, weight=1)
# tb_statistic.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)


# optionmenu_var = ctk.StringVar(value="1")  # set initial value

# def optionmenu_callback(choice):
#     print("optionmenu dropdown clicked:", float(choice)+1)

# combobox = ctk.CTkOptionMenu(master=app,
#                                        values=["1", "1.5","2","2.5", "3","3.5"],
#                                        command=optionmenu_callback,
#                                        variable=optionmenu_var)
# label_combo = ctk.CTkLabel(master = app,text='Доверительный коэф.', font=("Arial",16))
# combobox.pack(padx=5, pady=20, anchor = "se", side = ctk.BOTTOM)
# label_combo.pack(padx=30, pady=20, anchor = "se", side = ctk.BOTTOM)


# fr.place(x=20,y=20)

# # table = Table(app)
# app.mainloop()
class Sheet_Obj(Sheet):
    def __init__(self,frame, **kwargs):
         super().__init__(frame, **kwargs)
         self.enable_bindings()
     #     self.extra_bindings([("all_select_events", self.sheet_select_event)])
         
         
    
            
         
