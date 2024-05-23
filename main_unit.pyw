import customtkinter as ctk
from helpGUI_funcs import *
from normalization_w import normalization_view
from parametres_w import parametres_view
from mark_normal_w import mark_normal_view
from regression_w import regression_view
from plead_w import plead_view
from about_w import about_view
from Frame import Frame
from PIL import ImageTk, Image
from tile import tile_btn
import constants as const
from constants import *
import myDialogs as Dialog
import data_global as Data
import pandas as pd
import statistic
from correlation_w import correlation_view
from idlelib.tooltip import Hovertip
import copy

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Прогнозирование стоимости жилья")
        center_window(self)
        ctk.set_default_color_theme("green")
        
        #---------------------------SETTING_WALLPAPER-------------------------------#
        
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        
        img_wallpaper = Image.open(path_wallpaper_image)
        img_wallpaper=img_wallpaper.resize((width,height))
        img_wallpaper=ctk.CTkImage(light_image=img_wallpaper,size=(width,height))
        canvas=ctk.CTkLabel(self,width=width,height=height,image = img_wallpaper, text='')
        canvas.place(x=0,y=0)
        
        #---------------------------SETTING_WALLPAPER-------------------------------#

        #---------------------------UP_MENU-------------------------------#
        up_menu_frame = Frame(self, height = 50, width = self.winfo_width(),fg_color = 'grey')
        up_menu_frame.pack(anchor = 'nw')
        up_menu_var = ctk.StringVar()
        up_menu = ctk.CTkSegmentedButton(master=up_menu_frame,
                                                     values=["Загрузить данные", "О программе", "Помощь"],
                                                     variable=up_menu_var,command=lambda v:variant_choise(up_menu_var.get()))
        up_menu.pack(anchor='nw')
        #---------------------------UP_MENU-------------------------------#


        #---------------------------LOAD_DATA_POPUP-------------------------------#

        def combobox_callback(choice):
            match choice:
                case 'Excel':
                    
                    filename = ctk.filedialog.askopenfilename(
                    title='Загрузить исходные данные',
                    initialdir='/',
                    filetypes=filetypes)
                    Data.init_data = pd.read_excel(filename, engine = "openpyxl",header = None).values.tolist()
                    Data.init_data_frame=pd.DataFrame(Data.init_data)
                    Data.regress_data_frame = copy.deepcopy(Data.init_data_frame)

                    Data.regress_data_frame=pd.DataFrame(Data.init_data)
                    #---------------------------SAVE_HEADERS-------------------------------#
                    Data.data_change = pd.read_excel(filename, engine = "openpyxl",header = None).values.tolist()
                    Data.HEADER_ROW = Data.data_change[0]
                    del(Data.HEADER_ROW[0])#.pop(0)#pop for del common cell
                    Data.HEADER_COL = Data.column(Data.data_change,0)
                    del(Data.HEADER_COL[0])
                    # #---------------------------SAVE_HEADERS-------------------------------#
                    
                    Data.normal_data = pd.read_excel(filename, engine = "openpyxl",header = None).values.tolist()
                    tile_normal.mode_enable(flag=Data.data_change!=[])
                    Data.normal_data = Data.del_header(Data.normal_data)
                    Data.correlation_data_frame = pd.DataFrame(Data.normal_data,columns = Data.HEADER_ROW)
                    tile_statistic.mode_enable(flag=Data.normal_data!=[])
                    tile_correlation.mode_enable(flag=Data.normal_data!=[])
                    tile_plead.mode_enable(flag=Data.GO_CORREL)
                    tile_regression.mode_enable(flag=Data.init_data!=[])
                    statistic.min_max_norm(Data.normal_data)

                        
                    
                    combobox.pack_forget()
                    up_menu_var.set('')
                
                case 'Ручной ввод':
                    hand_load = Dialog.your_load(self)
                    combobox.pack_forget()
                    up_menu_var.set('')
                    
                
                case _:  
                    pass
        
            
        
        combobox_var = ctk.StringVar(value='Тип загрузки')
        combobox = ctk.CTkComboBox(master=up_menu_frame,
        # values=["Excel", "Ручной ввод"],state='readonly',
        values=["Excel"],state='readonly',
        command=combobox_callback,
        variable=combobox_var)
        
        #---------------------------LOAD_DATA_POPUP-------------------------------#

        #--------------------------CHOISE_MAIN_MENU----------------------------#
            
        def variant_choise(choise_str):
            match choise_str:
                case "Загрузить данные":
                    combobox.pack(anchor='nw')
                            
                case "О программе":
                    about_view()
                    up_menu_var.set('') 
                    
                case "Помощь":
                    pass 
                case _:  
                    pass
        #--------------------------CHOISE_MAIN_MENU----------------------------#


        #---------------------------TILES_FRAME-------------------------------#

        tiles_frame = Frame(self, height = self.winfo_height()-500,width = self.winfo_width()-500,fg_color = 'grey')
        tiles_frame.pack(anchor = ctk.CENTER, pady=100)
        #tiles_frame.config_grid(5,2,1,1)
        #---------------------------TILES_FRAME-------------------------------#


        #---------------------------TILES_BUTTONS-------------------------------#
        
        #-----TILE_NORMAL_BUTTON-----#
        
        img_normal = ctk.CTkImage(light_image=Image.open(path_normal_image),size=(100, 100))
        

        tile_normal = tile_btn(tiles_frame, text = 'Нормализация', command=lambda:normalization_view(self), image = img_normal, width = 300,
                                height = 50,compound=ctk.TOP,state=ctk.DISABLED)
        tile_normal.get_random_color()
        #-----TILE_NORMAL_BUTTON-----#


        #-----TILE_STATISTIC_BUTTON-----#

        img_parametres = ctk.CTkImage(light_image=Image.open(path_parametres_image),size=(100, 100))
        tile_statistic = tile_btn(tiles_frame, text = 'Статистические параметры', command=lambda:parametres_view(tile_mark_normal),
                                   image = img_parametres, width = 300, height = 50,compound=ctk.TOP,state=ctk.DISABLED) 
        tile_statistic.get_random_color()
       

        #-----TILE_STATISTIC_BUTTON-----#


        #-----TILE_MARK_NORMAL-----#
        img_mark_normal = ctk.CTkImage(light_image=Image.open(path_normal_mark_image),size=(100, 100))
        tile_mark_normal = tile_btn(tiles_frame, text = 'Оценка нормальности', command=lambda:mark_normal_view(),
                                   image = img_mark_normal, width = 300, height = 50,compound=ctk.TOP,state=ctk.DISABLED) 
        tile_mark_normal.get_random_color()
       
        #-----TILE_MARK_NORMAL-----#


        #-----TILE_CORRELATION_NORMAL-----#

        def go_correl():
            correlation_view()
            tile_plead.mode_enable(flag=True)
        img_correlation = ctk.CTkImage(light_image=Image.open(path_correlation_image),size=(100, 100))
        tile_correlation = tile_btn(tiles_frame, text = 'Корреляционный анализ', command=lambda:go_correl(),
                                   image = img_correlation, width = 300, height = 50,compound=ctk.TOP,state=ctk.DISABLED) 
        tile_correlation.get_random_color()

        #-----TILE_CORRELATION_NORMAL-----#


        #-----TILE_PLEAD-----#

        img_plead = ctk.CTkImage(light_image=Image.open(path_plead_image),size=(100, 100))
        tile_plead = tile_btn(tiles_frame, text = 'Корреляционные плеяды', command=lambda:plead_view(),
                                   image = img_plead, width = 300, height = 50,compound=ctk.TOP,state=ctk.DISABLED) 
        tile_plead.get_random_color()

        #-----TILE_PLEAD-----#


        #-----TILE_REGRSSION-----#
        img_regrssion = ctk.CTkImage(light_image=Image.open(path_regression_image),size=(100, 100))
        tile_regression = tile_btn(tiles_frame, text = 'Линейная регрессия', command=lambda:regression_view(),
                                   image = img_regrssion, width = 300, height = 50,compound=ctk.TOP,state=ctk.DISABLED) 
        tile_regression.get_random_color()




        #-----TILE_REGRSSION-----#

        #----------------------------POPUPS---------------------------------------#
        Hovertip(tile_normal,'Если вкладка неактивна-загрузите данные')
        Hovertip(tile_statistic,'Если вкладка неактивна-загрузите данные')
        Hovertip(tile_mark_normal,'Если вкладка неактивна-загрузите данные\n и прогрузите вкладку "Статистические параметры"')
        Hovertip(tile_correlation,'Если вкладка неактивна-загрузите данные')
        Hovertip(tile_plead,'Если вкладка неактивна-загрузите данные\n и прогрузите вкладку "Корреляционный анализ"')
        Hovertip(tile_regression,'Если вкладка неактивна-загрузите данные')
        
        tile_normal.grid(row=0, column=0, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        tile_statistic.grid(row=0, column=1, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        tile_mark_normal.grid(row=1, column=0, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        tile_correlation.grid(row=1, column=1, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        tile_plead.grid(row=0, column=2, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        tile_regression.grid(row=1, column=2, ipadx=6, ipady=6, padx=4, pady=4, sticky=ctk.NSEW)
        #---------------------------TILES_BUTTONS-------------------------------#

            

         
app = App()
app.mainloop()

