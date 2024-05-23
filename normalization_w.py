import customtkinter as ctk
from sheet_class import Sheet_Obj
from Frame import Frame
from helpGUI_funcs import *
import pandas as pd
import data_global as Data
import constants as const

class normalization_view(ctk.CTkToplevel):
    def __init__(self,root):
        super().__init__()
        self.title("Нормализация")
        self.configure(fg_color=const.colors_dict['cream'])
        center_window(self,1)
        

        #---------------------------INIT_DATA_FRAME--------------------------------------#
        frame_init_data_table = Frame(master = self, width = 1000, height = 600)
        sheet_init_data = Sheet_Obj(frame_init_data_table, data=Data.init_data, width=800, height=600)
        # frame_init_data_table.pack(anchor = 'w',pady=300)
        init_data_label = ctk.CTkLabel(frame_init_data_table,text='Исходные данные',font=('Arial',13))
        init_data_label.pack()
        sheet_init_data.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)
        #---------------------------INIT_DATA_FRAME--------------------------------------#



        #---------------------------NORMAL_DATA_FRAME--------------------------------------#
        frame_normal_data_table = Frame(master = self, width = 1000, height = 600)
        sheet_normal_data = Sheet_Obj(frame_normal_data_table, data=Data.normal_data, width=800, height=600)
        normal_data_label = ctk.CTkLabel(frame_normal_data_table,text='Нормализованные данные',font=('Arial',13))
        normal_data_label.pack()
        sheet_normal_data.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)

        #---------------------------NORMAL_DATA_FRAME--------------------------------------#

        #------------------------------PACK_FRAMES---------------------------------------#
        frame_init_data_table.pack(side = ctk.LEFT)
        frame_normal_data_table.pack(side = ctk.RIGHT)
        #------------------------------PACK_FRAMES---------------------------------------#
        
        self.grab_set()
        self.focus_set()
        self.wait_window()


        