import customtkinter as ctk
from sheet_class import Sheet_Obj
from Frame import Frame
from helpGUI_funcs import *
import pandas as pd
from scipy.stats import chisquare
import data_global as Data
import constants as const
import statistic
import plotting as plt
# from custom_hovertip import CustomTooltipLabel
from idlelib.tooltip import Hovertip

class mark_normal_view(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Оценка нормальности")
        self.configure(fg_color=const.colors_dict['cream'])
        center_window(self,1)
        
        #---------------------INIT_DATA_TO_TABLE-------------------#
        data_mark_normal = [[0] * (len(Data.HEADER_ROW)+1) for i in range(len(const.HEAD_COL_MARK_NORMAL))]#+1 for header col
        new_header_row = [""]+Data.HEADER_ROW
       
        #---------------------INIT_DATA_TO_TABLE-------------------#


        #---------------------------INIT_DATA_FRAME--------------------------------------#
        frame_init_data_table = Frame(master = self, width=self.winfo_width(), height = 350)
        sheet_mark_data = Sheet_Obj(frame_init_data_table, data=data_mark_normal, width=self.winfo_width(), height=300)

        #---------------------COLLECT_DATA_TO_TABLE-------------------#
        sheet_mark_data.set_row_data(0, values = tuple(new_header_row), add_columns = True, redraw = False)
        sheet_mark_data.set_column_data(0, values = tuple(const.HEAD_COL_MARK_NORMAL), add_rows = True, redraw = False)
        #---------------------COLLECT_DATA_TO_TABLE-------------------#



        #---------------------BUTTON_PARAMETRES-------------------#
        def load_params():
            for i in range(len(Data.parametres_data)):
                sheet_mark_data.insert_row(values = None, idx = "end", height = None, deselect_all = False, add_columns = False,
                    redraw = False)
                sheet_mark_data.set_row_data(i+6, values = tuple(Data.parametres_data[i-6]), add_columns = True, redraw = False)
            paramtres_btn.configure(state=ctk.DISABLED)


        paramtres_btn = ctk.CTkButton(frame_init_data_table, text='Выгрузка статистических параметров', font = ('Arial',13),
                                      command=lambda:load_params())
        #---------------------BUTTON_PARAMETRES-------------------#

        #---------------------------------PLOTTING_FRAME---------------------------------------#
        main_plotting = ctk.CTkScrollableFrame(master = self, width=self.winfo_width(), height = 550)
        # main_plotting.add_scroll()
        df = pd.DataFrame(Data.init_data)
        df = Data.prepare_dataframe(df)
        #---------------------------------PLOTTING_FRAME---------------------------------------#

        
        df = pd.DataFrame(Data.normal_data)
        #drop first str header
        df.drop(index=df.index [0], axis= 0 , inplace= True )

        for j in range(1,len(Data.HEADER_ROW)+1):
            
            mean = statistic.mean(df[j].to_list())
            wait_data = [mean for i in range(len(df[j].to_list()))]
            #Pirson = (chisquare(df[j].to_list(), f_exp=wait_data))
            Pirson = statistic.Xi_square(wait_data=wait_data,emp_data=df[j].to_list())
            #Pirson = round(Pirson.statistic, 3)
            Pirson = round(Pirson, 3)
            #cell_data_Xi = round(Xi_sqrt.statistic, 3)
            cell_data_Xi = Pirson = round(Pirson, 3)
            
            sheet_mark_data.set_cell_data(1, j, value = cell_data_Xi, set_copy = True, redraw = True)
            
            
            if Pirson <=const.CRITICAL_PIRSON:
                sheet_mark_data.set_cell_data(5, j, value = '+', set_copy = True, redraw = True)
                sheet_mark_data.highlight_cells(row = 5, column = j, cells = [], canvas = "table", bg = const.colors_dict['green'], fg = None,
                                                 redraw = False, overwrite = True)
            else:
                sheet_mark_data.set_cell_data(5, j, value = '-', set_copy = True, redraw = True)
                
        

        #critical Pirson value row in data table
        for j in range(1,len(Data.HEADER_ROW)+1):
            sheet_mark_data.set_cell_data(2, j, value = const.CRITICAL_PIRSON, set_copy = True, redraw = True)        

        
        #statistic about interval
        for j in range(1,len(Data.HEADER_ROW)+1):
            sheet_mark_data.set_cell_data(3, j, value = statistic.lst_to_str(statistic.interval_series(df[j].to_list()),' '),
                                           set_copy = True, redraw = True)
            
            

            #create sub frame for plotting each data in dataframe

            sub_frame1 = Frame(master = main_plotting, width=self.winfo_screenwidth(), height = 550)
            title1 = ctk.CTkLabel(sub_frame1,text=str(Data.HEADER_ROW[j-1]),font=('Arial',13))
            y = statistic.interval_series(df[j].to_list())
            x = statistic.get_middle()
            plt.interval_mark(master = sub_frame1,x=x,y=y)
            title1.pack()
            sub_frame1.pack(anchor='w',fill=ctk.BOTH)
            
        #borders of intervals
        for j in range(1,len(Data.HEADER_ROW)+1):
            sheet_mark_data.set_cell_data(4, j, value = statistic.get_borders(df[j].to_list()),
                                           set_copy = True, redraw = True)
        #---------------------COLLECT_DATA_TO_TABLE-------------------#

        init_data_label = ctk.CTkLabel(frame_init_data_table,text='Оценка нормальности',font=('Arial',13))
        init_data_label.pack()
        sheet_mark_data.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)
        #---------------------------INIT_DATA_FRAME--------------------------------------#
        #------------------------------PACK_FRAMES---------------------------------------#
        paramtres_btn.pack(anchor='se',pady=5)
        frame_init_data_table.pack(side = ctk.TOP)
        # paramtres_btn.pack(anchor='se',pady=5)
        main_plotting.pack(side=ctk.TOP,pady=10)
        #------------------------------PACK_FRAMES---------------------------------------#
        
        self.grab_set()
        self.focus_set()
        self.wait_window()