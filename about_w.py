import customtkinter as ctk
from Frame import Frame
from helpGUI_funcs import *
import constants as const

class about_view(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("О программе")
        self.configure(fg_color=const.colors_dict['cream'])
        center_window(self,1)
        text = ctk.CTkTextbox(master=self,width=self.winfo_width(),height=self.winfo_height())
        data = open(const.path_about_text,'r')
        data = data.read()
        text.insert("0.0", data)
        text.configure(state = ctk.DISABLED)
        text.pack()