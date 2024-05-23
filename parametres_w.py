import customtkinter as ctk
from helpGUI_funcs import *
import constants as const
from Frame import Frame
from sheet_class import Sheet_Obj
import data_global as Data
import statistic
from math import sqrt



class parametres_view(ctk.CTkToplevel):
    def __init__(self,tile):
        super().__init__()
        self.title("Обзор статистических параметров")
        self.configure(fg_color=const.colors_dict['cream'])
        center_window(self,1)

        # print(Data.normal_data_frame)
        # print(Data.HEADER_ROW)
        #---------------------------COLLECT_DATA_PARAMETRES---------------------------#
        new_header_row = [''] + Data.HEADER_ROW
        

        data_parametres = [[0] * len(new_header_row) for i in range(len(const.HEAD_COL_PARAM))]

        
        #---------------------------COLLECT_DATA_PARAMETRES---------------------------#

        #---------------------------PARAM_DATA_FRAME--------------------------------------#
        frame_param_data_table = Frame(master = self, width = self.winfo_width(), height = 360)
        sheet_param_data = Sheet_Obj(frame_param_data_table, data=data_parametres, width=self.winfo_width(), height=360)

        #---------------------------INSERT_DATA-------------------------------------#

        sheet_param_data.set_row_data(0, values = tuple(new_header_row), add_columns = True, redraw = False)
        sheet_param_data.set_column_data(0, values = tuple(const.HEAD_COL_PARAM), add_rows = True, redraw = False)

        for i in range(1,len(const.HEAD_COL_PARAM)):
            for j in range(1,len(Data.HEADER_ROW)+1):
                cell_data = statistic.func_list[i-1](Data.normal_data_frame[Data.HEADER_ROW[j-1]].to_list())
                cell_data = round(cell_data,3)
                sheet_param_data.set_cell_data(i, j, value = cell_data, set_copy = True, redraw = False)
        
        tmp_data = sheet_param_data.get_sheet_data(return_copy = False, get_header = False, get_index = False)
        Data.parametres_data = tmp_data[:]
        #Data.parametres_data = Data.parametres_data.pop(0)
        del Data.parametres_data[0]
        
        tile.mode_enable(flag=Data.parametres_data!=[])
    
        
        #---------------------------INSERT_DATA-------------------------------------#
        
        param_data_label = ctk.CTkLabel(frame_param_data_table,text='Статистические параметры',font=('Arial',13))
        param_data_label.pack()
        sheet_param_data.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)
        
        #---------------------------PARAM_DATA_FRAME--------------------------------------#

        #---------------------ERRORS_AND_VOLUME_DATA_FRAME--------------------------------#
        frame_error_data_table = Frame(master = self, width = self.winfo_width(), height = 360)

        #---------------------------INIT_DATA-------------------------------------#
        data_errors = [[0] * len(new_header_row) for i in range(len(const.HEAD_COL_ERROR))]
        #---------------------------INIT_DATA-------------------------------------#


        sheet_error_data = Sheet_Obj(frame_error_data_table, data=data_errors, width=self.winfo_width(), height=360)

        #---------------------------INSERT_DATA-------------------------------------#
        sheet_error_data.set_row_data(0, values = tuple(new_header_row), add_columns = True, redraw = False)
        sheet_error_data.set_column_data(0, values = tuple(const.HEAD_COL_ERROR), add_rows = True, redraw = False)


        #Get data of dispersion from param sheet
        dispers = sheet_param_data.get_row_data(const.index_variance, return_copy = True)
        dispers = list(dispers)
        dispers.pop(0)
        dispers  = list(map(float, dispers))
        
        
        #len of data
        len_data = len(Data.normal_data_frame[Data.HEADER_ROW[0]].to_list())
        #insert mean error
        for j in range(1,len(Data.HEADER_ROW)+1):
            cell_data = sqrt(dispers[j-1]/50)
            cell_data = round(cell_data,3)
            sheet_error_data.set_cell_data(1, j, value = cell_data, set_copy = True, redraw = False)


        #---------------------------INSERT_DATA-------------------------------------#
        # frame_init_data_table.pack(anchor = 'w',pady=300)
        error_data_label = ctk.CTkLabel(frame_error_data_table,text='Предельная ошибка и объем выборки',font=('Arial',13))
        error_data_label.pack()
        sheet_error_data.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)

        #---------------------ERRORS_AND_VOLUME_DATA_FRAME--------------------------------#


        #------------------------------KOEF_COMBOBOX-----------------------------------------#
        optionmenu_var = ctk.StringVar(value="1")  # set initial value

        #insert limit error
        for j in range(1,len(Data.HEADER_ROW)+1):
            #get cell mean error
            cell_mean_error = float(sheet_error_data.get_cell_data(1, j, return_copy = True))
            koef = float(optionmenu_var.get())  
            cell_data = cell_mean_error * koef
            cell_data = round(cell_data,3)
            sheet_error_data.set_cell_data(2, j, value = cell_data, set_copy = True, redraw = False)

        #insert valume size
        for j in range(1,len(Data.HEADER_ROW)+1):
            #get cell mean error
            cell_limit_error = float(sheet_error_data.get_cell_data(2, j, return_copy = True))
            koef = float(optionmenu_var.get())
            cell_data = len_data * koef**2*dispers[j-1]/(len_data * cell_limit_error**2 + koef**2 * dispers[j-1]) 
            cell_data = round(cell_data,3)
            sheet_error_data.set_cell_data(3, j, value = cell_data, set_copy = True, redraw = False)

        

        def optionmenu_callback(choice):
            pass

        def refresh_limit_error():
            #insert limit error
            koef = float(optionmenu_var.get())
            for j in range(1,len(Data.HEADER_ROW)+1):
                #get cell mean error
                cell_mean_error = float(sheet_error_data.get_cell_data(1, j, return_copy = True))
                cell_data = cell_mean_error * koef
                cell_data = round(cell_data,3)
                sheet_error_data.set_cell_data(2, j, value = cell_data, set_copy = True, redraw = True)
            sheet_error_data.highlight_rows(rows = [2], bg = const.colors_dict['green'], fg = None, highlight_index = True,
                                             redraw = False, end_of_screen = False, overwrite = True)
            
            #insert valume size
            for j in range(1,len(Data.HEADER_ROW)+1):
                #get cell mean error
                cell_limit_error = float(sheet_error_data.get_cell_data(2, j, return_copy = True))
                koef = float(optionmenu_var.get())
                cell_data = len_data * koef**2*dispers[j-1]/(len_data * cell_limit_error**2 + koef**2 * dispers[j-1]) 
                cell_data = round(cell_data,3)
                sheet_error_data.set_cell_data(3, j, value = cell_data, set_copy = True, redraw = False)
            sheet_error_data.highlight_rows(rows = [3], bg = const.colors_dict['green'], fg = None, highlight_index = True,
                                             redraw = False, end_of_screen = False, overwrite = True)
            
            

        combobox = ctk.CTkOptionMenu(master=self,
                                               values=["1", "1.5","2","2.5", "3","3.5"],
                                               command=optionmenu_callback,
                                               variable=optionmenu_var)
        label_combo = ctk.CTkLabel(master = self,text='Доверительный коэф.', font=("Arial",13))
        
        #------------------------------KOEF_COMBOBOX-----------------------------------------#


        #------------------------------CALCULATE_WIDGETS-----------------------------------------#
        # label_calculate = ctk.CTkLabel(master = self,text='Расчитать предельную ошибку.', font=("Arial",13))
        button_calculate = ctk.CTkButton(master = self, text='Рассчитать предельную ошибку', font =("Arial",13),command=refresh_limit_error)
        #------------------------------CALCULATE_WIDGETS-----------------------------------------#


        #---------------------------GRID_FRAMES--------------------------------------#
        frame_param_data_table.grid(row=0,column=0,pady=15)
        frame_error_data_table.grid(row=1,column=0,pady=10)

        label_combo.grid(row=2,column=0,pady=5,padx=15,sticky='se')
        combobox.grid(row=3,column=0,pady=5,padx = 15,sticky='se')

       # label_calculate.grid(row=4,column=0,pady=5,padx=10,sticky='se')
        button_calculate.grid(row=5,column=0,pady=5,padx=10,sticky='se')
        #---------------------------GRID_FRAMES--------------------------------------#