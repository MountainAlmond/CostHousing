import customtkinter as ctk
# from sheet_class import Sheet_Obj
from Frame import Frame
from helpGUI_funcs import *
from mark_regression_view import mark_regression_view
import pandas as pd
import data_global as Data
import constants as const
import plotting as plt
from sheet_class import Sheet_Obj
import matrix_ops
from math import sqrt
import copy
import data_global as Data
import matrix_ops
import statistic
import statsmodels.api as sm



class regression_view(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Линейная регрессия")
        self.configure(fg_color=const.colors_dict['cream'])
        center_window(self,1)
        
        regression_df = copy.deepcopy(Data.regress_data_frame)
        regression_df = regression_df.drop(labels = [0],axis = 0)
        regression_df = regression_df.astype(float)
        Data.regression_df_final = copy.deepcopy(regression_df)
        y = regression_df[1]
        x = regression_df[[2,3,4,5,6,7,8]]
        x = sm.add_constant(x)
        model = sm.OLS(y, x).fit()
        koefs = model.params.tolist()

        Data.koefs_regression = koefs
        # print(model.summary())


        #form data for regression koef
        REGRES_HEADER = ['B0','B1','B2','B3','B4','B5','B6','B7']
        Data.regress_data_frame = Data.regress_data_frame.drop(labels=0,axis=0)
        Data.regress_data_frame = Data.regress_data_frame.drop(labels=0,axis=1)
        
        frame_regression_matrix = Frame(master = self, width=self.winfo_width(), height = 250)
        frame_regression_final = Frame(master = self, width=self.winfo_width(), height = 100)
        
        data_matrix_regression = [[0 for i in range(len(REGRES_HEADER)+1)] for j in range(3)]#+1 for headers


        #insert head column of regression
        for i in range(len(const.HEAD_COL_REGRESSION)):
            data_matrix_regression[i][0] = const.HEAD_COL_REGRESSION[i]

        for i in range(1,len(REGRES_HEADER)+1):
            data_matrix_regression[0][i] = REGRES_HEADER[i-1]
            data_matrix_regression[1][i] = Data.HEADER_ROW[i-1]
       
        for i in range(1,len(REGRES_HEADER)+1):
            data_matrix_regression[2][i] = round(koefs[i-1],3)
            
        frame_calculate = Frame(master = self, width=self.winfo_width(), height = 400,border_width=10,border_color='gold')

        entry_lst = []
        for i in range(1,len(Data.HEADER_ROW)):
            label = ctk.CTkLabel(master = frame_calculate, text=Data.HEADER_ROW[i],font=('Arial',13))
            entry = ctk.CTkEntry(master= frame_calculate)
            entry_lst.append(entry)
            label.grid(column=0,row=i,padx=5,pady=5)
            entry.grid(column=1,row=i,padx=5,pady=5)
        
        def calculate_prediction_val():
            res = 0
            for i in range(1,len(entry_lst)+1):
                res = res + float(entry_lst[i-1].get())*data_matrix_regression[2][i+1]
            res = res + data_matrix_regression[2][1]
            res = round(res,2)
            prediction_entry.delete(0, 'end')
            prediction_entry.insert(ctk.END, res)


        prediction_btn = ctk.CTkButton(master = frame_calculate,text='Рассчитать уровень безработицы', font=('Arial',13)
                                       ,command=lambda:calculate_prediction_val())
        prediction_entry = ctk.CTkEntry(master=frame_calculate)
        prediction_btn.grid(column=0,row=8,padx=5,pady=5)
        prediction_entry.grid(column=1,row=8,padx=5,pady=5)


        label_regression = ctk.CTkLabel(master = frame_regression_matrix, text='Коэффициенты регрессии', font=('Arial',13))
        
        label_regression.pack()
        sheet_regression_data = Sheet_Obj(frame_regression_matrix, data=data_matrix_regression, width=self.winfo_width(), height=250)
        sheet_regression_data.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)



        #----------------------------------------------Sheet final of regrission analyze----------------------------------------------#
        data_matrix_regression_final = [[0 for i in range(2)] for j in range(len(const.HEAD_COL_REGRESSION_FINAL))]#+1 for headers
        for i in range(len(const.HEAD_COL_REGRESSION_FINAL)):
            data_matrix_regression_final[i][0] = const.HEAD_COL_REGRESSION_FINAL[i]
            
            
        data_matrix_regression_final[0][1] = float(round(model.rsquared,3))
        data_matrix_regression_final[1][1] = round(model.fvalue,3)
        data_matrix_regression_final[2][1] = const.CRITICAL_FISHER
        data_matrix_regression_final[3][1] = const.DATA_LENGTH

        #----------------------------------------------Sheet final of regrission analyze----------------------------------------------#

        #----------------------------------------------pack widgets regression frame----------------------------------------------#
        label_regression_final = ctk.CTkLabel(master = frame_regression_final, text='Сводные данные по регрессии', font=('Arial',13))
        
        label_regression_final.pack()
        sheet_regression_data_final = Sheet_Obj(frame_regression_final, data=data_matrix_regression_final, width=self.winfo_width(), height=250)
        sheet_regression_data_final.pack(anchor='center', fill=ctk.X,side=ctk.BOTTOM)

        mark_regress_btn = ctk.CTkButton(master = frame_regression_final,text='Графически оценить\n точность регрессии',font=('Arial',13),
                                         command=lambda:mark_regression_view())
        mark_regress_btn.pack(anchor='nw')

        frame_regression_matrix.grid(column=0,row=0,pady=5,padx=5)
        frame_regression_final.grid(column=0,row=1,pady=5,padx=5)
        frame_calculate.grid(column=0,row=2,pady=5,padx=5)