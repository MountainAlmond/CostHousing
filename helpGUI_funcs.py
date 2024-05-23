import customtkinter as ctk


#---------------------------HELP_MAPPING_FUNCS-------------------------------#
def center_window(window,val_top=0):
    window.w, window.h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry("{0}x{1}-10+0".format(window.w, window.h))
    window.resizable(width=False, height=False)
    window.attributes('-topmost', val_top)
#---------------------------HELP_MAPPING_FUNCS-------------------------------#


    
    


