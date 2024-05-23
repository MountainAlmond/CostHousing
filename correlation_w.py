import customtkinter as ctk
# from sheet_class import Sheet_Obj
from Frame import Frame
from helpGUI_funcs import *
import pandas as pd
from scipy.stats import chisquare
import data_global as Data
import constants as const
import statistic
import plotting as plt
from sheet_class import Sheet_Obj
import matrix_ops
from math import sqrt
import copy


# from custom_hovertip import CustomTooltipLabel
# from idlelib.tooltip import Hovertip

class correlation_view(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Корреляционный анализ")
        self.configure(fg_color=const.colors_dict['cream'])
        center_window(self,1)


        #prepare Dataframe (delete headers)
        if Data.GO_CORREL:

            Data.init_data_frame = Data.init_data_frame.drop(labels=0,axis=0)
            Data.init_data_frame = Data.init_data_frame.drop(labels=0,axis=1)
            Data.GO_CORREL=False

        


        common_frame = ctk.CTkScrollableFrame(master=self,width=self.winfo_width(),height=self.winfo_height())

        #-----------------------------PAIR_CORRELATION------------------------------------------#
        frame_correlation_matrix = Frame(master = common_frame, width=self.winfo_width(), height = 222)

        #get matrix of pair-correlation for input Dataframe

        data_matrix_pair_correl = [[0 for i in range(9)] for j in range(9)]#+1 for headers
        
        for i in range(0,len(Data.HEADER_ROW)):
            data_matrix_pair_correl[0][i+1] = Data.HEADER_ROW[i]
            data_matrix_pair_correl[i+1][0] = Data.HEADER_ROW[i]


        data_matrix_pair_correl[0][0]=''
        

        label_pair_correl = ctk.CTkLabel(master = frame_correlation_matrix, text='Матрица парных корреляций', font=('Arial',13))
        
        label_pair_correl.pack()
        sheet_pair_correl = Sheet_Obj(frame_correlation_matrix, data=data_matrix_pair_correl, width=self.winfo_width(), height=222)
        for i in range(1, len(Data.HEADER_ROW)+1):
            for j in range(1,len(Data.HEADER_ROW)+1):
                if (i<=8):
                    data_matrix_pair_correl[i][j] = statistic.get_Pirson_correlation(Data.init_data_frame.iloc[:,i-1].to_list(),
                                                                                 Data.init_data_frame.iloc[:,j-1].to_list())
        #highlight cells            
        for i in range(1, len(Data.HEADER_ROW)+1):
            for j in range(1,len(Data.HEADER_ROW)+1):
                if(abs(data_matrix_pair_correl[i][j])<0.3):
                    sheet_pair_correl.highlight_cells(row = i, column = j, cells = [], canvas = "table", bg = 'green',
                                                     fg = None, redraw = False, overwrite = True)
                            
                if(abs(data_matrix_pair_correl[i][j])>=0.3 and abs(data_matrix_pair_correl[i][j])<=0.6):
                    sheet_pair_correl.highlight_cells(row = i, column = j, cells = [], canvas = "table", bg = 'blue',
                                                     fg = None, redraw = False, overwrite = True)
                            
                if(abs(data_matrix_pair_correl[i][j])>=0.6 and abs(data_matrix_pair_correl[i][j])<=0.7):
                    sheet_pair_correl.highlight_cells(row = i, column = j, cells = [], canvas = "table", bg = 'orange',
                                                     fg = None, redraw = False, overwrite = True)
                            
                if(abs(data_matrix_pair_correl[i][j])>0.7):
                    sheet_pair_correl.highlight_cells(row = i, column = j, cells = [], canvas = "table", bg = 'red',
                                                     fg = None, redraw = False, overwrite = True)
        sheet_pair_correl.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)


        matrix_pair_correl_s = copy.deepcopy(data_matrix_pair_correl)
        matrix_pair_correl_s = matrix_ops.get_minor(matrix_pair_correl_s,0,0)
        Data.pair_correl_matrix = matrix_pair_correl_s

        

        #-----------------------------PAIR_CORRELATION------------------------------------------#

        #----------------------------the Student's significance level--------------------------------------#
        frame_students = Frame(master = common_frame, width=self.winfo_width(), height = 222)

        data_students = [[0 for i in range(9)] for j in range(9)]#+1 for headers

        for i in range(0,len(Data.HEADER_ROW)):
            data_students[0][i+1] = Data.HEADER_ROW[i]
            data_students[i+1][0] = Data.HEADER_ROW[i]


        data_students[0][0]=''

        for i in range(1, len(Data.HEADER_ROW)+1):
            for j in range(1,len(Data.HEADER_ROW)+1):
                if (i<=8) and (i!=j):
                    #  data_students[i][j] = round(statistic.get_Student_pair_koef(Data.init_data_frame.iloc[:,i-1].to_list(),
                    #                                                               Data.init_data_frame.iloc[:,j-1].to_list()),2)
                    data_students[i][j] = round(statistic.get_Student_pair_koef(matrix_pair_correl_s[i-1][j-1]),2)
                if (i==j):
                    data_students[i][j]='\u221e'




        label_student = ctk.CTkLabel(master = frame_students, text='Критерий Стьюдента для парных корреляций', font=('Arial',13))

        sheet_students = Sheet_Obj(frame_students, data=data_students, width=self.winfo_width(), height=222)
        
        label_student.pack()
        for i in range(1, len(Data.HEADER_ROW)+1):
            for j in range(1,len(Data.HEADER_ROW)+1):
                if (i<=8) and (i!=j):
                    if(abs(data_students[i][j])>const.CRITICAL_STUDENT):
                        sheet_students.highlight_cells(row = i, column = j, cells = [], canvas = "table", bg = 'green',
                                                     fg = None, redraw = False, overwrite = True)
                            
                    

        sheet_students.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)


        #----------------------------the Student's significance level--------------------------------------#



        #---------------------------------PERSONAL_CORRELATION------------------------------------------#
        frame_personal_correlation_matrix = Frame(master = common_frame, width=self.winfo_width(), height = 222)

        #get matrix of pair-correlation for input Dataframe

        data_matrix_personal_correl = [[0 for i in range(9)] for j in range(9)]#+1 for headers
        
        for i in range(0,len(Data.HEADER_ROW)):
            data_matrix_personal_correl[0][i+1] = Data.HEADER_ROW[i]
            data_matrix_personal_correl[i+1][0] = Data.HEADER_ROW[i]


        data_matrix_personal_correl[0][0]=''
        matrix_data = copy.deepcopy(data_matrix_pair_correl)
        matrix_data = matrix_ops.get_minor(data_matrix_pair_correl,0,0)
    
       
        for i in range(1, len(Data.HEADER_ROW)+1):
            for j in range(1,len(Data.HEADER_ROW)+1):
                if (i<=8) and (i!=j):
                    #get minors
                    copy1 = copy.deepcopy(matrix_data)
                    Mij = matrix_ops.get_minor(copy1,i-1,j-1)
                    copy2 = copy.deepcopy(matrix_data)
                    Mii = matrix_ops.get_minor(copy2,i-1,i-1)
                    copy3 = copy.deepcopy(matrix_data)
                    Mjj = matrix_ops.get_minor(copy3,j-1,j-1)

                    Rij = matrix_ops.determinant(Mij)*((-1)**(i-1+j-1))
                    Rii = matrix_ops.determinant(Mii)*((-1)**(i-1+i-1))
                    Rjj = matrix_ops.determinant(Mjj)*((-1)**(j-1+j-1))
                    

                    data_matrix_personal_correl[i][j] = Rij/sqrt(Rii*Rjj)
                    
                    

                    #---------------TEST------------------------#
                    # det_matrix = matrix_ops.determinant(matrix_data)
                    # copy1 = copy.deepcopy(matrix_data)
                    # Mii = matrix_ops.get_minor(copy1,i-1,i-1)
                    # Aii = matrix_ops.determinant(Mii)*(-1)**(i-1+i-1)
                    # data_matrix_personal_correl[i][j] = sqrt(1-(abs(det_matrix)/Aii))

                    
                if(i==j):
                    data_matrix_personal_correl[i][j]=1

         #send personal correl for global data
        matrix_personal_correl_s = copy.deepcopy(data_matrix_personal_correl)
        matrix_personal_correl_s = matrix_ops.get_minor(matrix_personal_correl_s,0,0)
        Data.personal_correl_matrix = matrix_personal_correl_s


            # step_matrix = step_matrix + 1


        label_personal_correl = ctk.CTkLabel(master = frame_personal_correlation_matrix,
                                              text='Матрица частных корреляций', font=('Arial',13))
        
        label_personal_correl.pack()
        sheet_pers_corr_data = Sheet_Obj(frame_personal_correlation_matrix, data=data_matrix_personal_correl,
                                          width=self.winfo_width(), height=222)
        for i in range(1, len(Data.HEADER_ROW)+1):
            for j in range(1,len(Data.HEADER_ROW)+1):
                if(abs(data_matrix_personal_correl[i][j])<0.3):
                    sheet_pers_corr_data.highlight_cells(row = i, column = j, cells = [], canvas = "table", bg = 'green',
                                                     fg = None, redraw = False, overwrite = True)
                            
                if(abs(data_matrix_personal_correl[i][j])>=0.3 and abs(data_matrix_personal_correl[i][j])<=0.6):
                    sheet_pers_corr_data.highlight_cells(row = i, column = j, cells = [], canvas = "table", bg = 'blue',
                                                     fg = None, redraw = False, overwrite = True)
                            
                if(abs(data_matrix_personal_correl[i][j])>0.6 and abs(data_matrix_personal_correl[i][j])<=0.7):
                    sheet_pers_corr_data.highlight_cells(row = i, column = j, cells = [], canvas = "table", bg = 'orange',
                                                     fg = None, redraw = False, overwrite = True)
                            
                if(abs(data_matrix_personal_correl[i][j])>0.7):
                    sheet_pers_corr_data.highlight_cells(row = i, column = j, cells = [], canvas = "table", bg = 'red',
                                                     fg = None, redraw = False, overwrite = True)
        sheet_pers_corr_data.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)



        #prepare for triangle correlation matrixs
        step = 1
        for i in range(1, len(Data.HEADER_ROW)+1):
            for j in range(len(Data.HEADER_ROW)+1,step,-1):
                # sheet_pers_corr_data.set_cell_data(i, j, value = " ", set_copy = True, redraw = False)
                # sheet_pair_correl.set_cell_data(i, j, value = "", set_copy = False, redraw = False)
                sheet_pers_corr_data.dehighlight_cells(row = i, column = j, cells = [], canvas = "table", all_ = False, redraw = True)
                sheet_pair_correl.dehighlight_cells(row = i, column = j, cells = [], canvas = "table", all_ = False, redraw = True)
            step = step + 1
            

        #---------------------------------PERSONAL_CORRELATION------------------------------------------#


        #---------------------------------PERSONAL_STUDENT'S------------------------------------------#
        frame_personal_students_matrix = Frame(master = common_frame, width=self.winfo_width(), height = 222)

        #get matrix of pair-correlation for input Dataframe

        data_matrix_personal_students = [[0 for i in range(9)] for j in range(9)]#+1 for headers
        
        for i in range(0,len(Data.HEADER_ROW)):
            data_matrix_personal_students[0][i+1] = Data.HEADER_ROW[i]
            data_matrix_personal_students[i+1][0] = Data.HEADER_ROW[i]

        n = const.DATA_LENGTH-2
        data_matrix_personal_students[0][0]=''
        for i in range(1, len(Data.HEADER_ROW)+1):
            for j in range(1,len(Data.HEADER_ROW)+1):
                if (i<=8) and (i!=j):
                    # data_matrix_personal_students[i][j] = sqrt(n/(1-matrix_data[i-1][j-1]**2))
                    data_matrix_personal_students[i][j] = round((sqrt(n)/sqrt(1-matrix_data[i-1][j-1]))*matrix_data[i-1][j-1],2)
                    #data_matrix_personal_students[i][j] = sqrt(19/(1-matrix_data[i-1][j-1]**2)*matrix_data[i-1][j-1])
                if(i==j):
                    data_matrix_personal_students[i][j]='\u221e'
        


        label_personal_students = ctk.CTkLabel(master = frame_personal_students_matrix,
                                              text='Критерий Стьюдента для частных корреляций', font=('Arial',13))
        
        label_personal_students.pack()
        sheet_pers_students_data = Sheet_Obj(frame_personal_students_matrix, data=data_matrix_personal_students,
                                          width=self.winfo_width(), height=222)
        sheet_pers_students_data.pack(expand=True,anchor='center', fill=ctk.X,side=ctk.BOTTOM)

        #highlight_cells of pers Student's
        for i in range(1, len(Data.HEADER_ROW)+1):
            for j in range(1,len(Data.HEADER_ROW)+1):
                if (i<=8) and (i!=j):
                    if(abs(data_matrix_personal_students[i][j])>const.CRITICAL_STUDENT):
                        sheet_pers_students_data.highlight_cells(row = i, column = j, cells = [], canvas = "table", bg = 'green',
                                                     fg = None, redraw = False, overwrite = True)




        #---------------------------------PERSONAL_STUDENT'S------------------------------------------#



        #---------------------------------CONTROL_FRAME------------------------------------------#
        
        #---------------------------------CONTROL_FRAME------------------------------------------#


        #-----------------------------POSITIONING_WIDGETS------------------------------------------#
        # control_frame.grid(column=0,row=0,padx=5,pady=5,sticky='w')
        common_frame.grid(column = 0, row = 0, padx = 5)
        frame_correlation_matrix.grid(column=0,row=0, padx=5)
        frame_students.grid(column=0,row=1, padx=5)
        frame_personal_correlation_matrix.grid(column=0,row=2, padx=5)
        frame_personal_students_matrix.grid(column=0,row=3, padx=5)

        # plead = ctk.CTkButton(master = common_frame, text = 'Посмотреть плеяды')
        
        # plead.grid(column=0,row=4, padx=5,pady=1)
        
        
        #-----------------------------POSITIONING_WIDGETS------------------------------------------#
