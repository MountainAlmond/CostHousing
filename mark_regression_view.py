import customtkinter as ctk
from sheet_class import Sheet_Obj
from Frame import Frame
from helpGUI_funcs import *
import pandas as pd
import data_global as Data
import constants as const
import copy
from plotting import mark_regression
# import statistic
# import plotting as plt
# from custom_hovertip import CustomTooltipLabel
from idlelib.tooltip import Hovertip

class mark_regression_view(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Оценка регрессии")
        self.configure(fg_color=const.colors_dict['cream'])
        center_window(self,1)
        #---------------------INIT_DATA_TO_TABLE-------------------#
        data_mark_regression = [[0] * (3) for i in range(const.DATA_LENGTH+2)]#+2 for header and avarage res of err 
        
        data_mark_regression[0][0] = 'Действ. значение'
        data_mark_regression[0][1] = 'Значение модели'
        data_mark_regression[0][2] = 'Погрешность'

        #---------------------INSERT_DATA_FINAL_REGRESSION-------------------#
        df = copy.deepcopy(Data.regress_data_frame)
        #row of dataframe to list
        # row = df.iloc[3].to_list()
        y = df[1].to_list()
        regress = copy.deepcopy(y)
        real = []
        avarage_err = 0
        sum_value = 0
        # print(y)
        # print(df)
        
        for i in range(1,const.DATA_LENGTH+1):
            data_mark_regression[i][0] = y[i-1]
            sum_value = sum_value + y[i-1] 

        for i in range(const.DATA_LENGTH):
            #get row of dataframe
            row = df.iloc[i].to_list()
            #delete y from row
            row.pop(0)
            # print(row)
            res = 0
            for j in range(1,len(Data.koefs_regression)):
                res = res + row[j-1]*Data.koefs_regression[j]
            #sum with b0 const koef of regression
            res = res + Data.koefs_regression[0]
            data_mark_regression[i+1][1] = round(res,2)
            real.append(res)
            data_mark_regression[i+1][2] = round(abs(data_mark_regression[i+1][0]-data_mark_regression[i+1][1]),2)
            avarage_err = avarage_err + data_mark_regression[i+1][2]
            

        #prepare data to avarage err
        data_mark_regression[const.DATA_LENGTH+1][0]='СРЕДНЯЯ ПОГРЕШНОСТЬ'
        data_mark_regression[const.DATA_LENGTH+1][1]=''
        data_mark_regression[const.DATA_LENGTH+1][2]=round(avarage_err/const.DATA_LENGTH,2)

        #---------------------INSERT_DATA_FINAL_REGRESSION-------------------#
        
        

        #---------------------------INIT_DATA_FRAMES--------------------------------------#
        frame_init_data_table = ctk.CTkScrollableFrame(master = self, width=500, height = self.winfo_height())
        sheet_mark_regression = Sheet_Obj(frame_init_data_table, data=data_mark_regression, width=400, height = self.winfo_height())
        sheet_mark_regression.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)


        frame_plot = Frame(master = self, width=self.winfo_width()-500, height = self.winfo_height())
        #-----------------------------PLOTTING-----------------------------------#
        mark_regression(frame_plot,regress,real)
        #-----------------------------PLOTTING-----------------------------------#
        
        #-------------------------FRAME_POSITIONS-------------------------#
        frame_init_data_table.grid(column=0,row=0,padx=5,pady=5)
        frame_plot.grid(column=1,row=0,padx=5,pady=5)
        #-------------------------FRAME_POSITIONS-------------------------#
        