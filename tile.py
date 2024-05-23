import customtkinter as ctk
from PIL import ImageTk, Image
from constants import colors
import random
#----------------TILE_BUTTON--------------------#
class tile_btn(ctk.CTkButton):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        #self.configure(image = img,command = lambda:func())

    def get_random_color(self):
        self.configure(fg_color = colors[random.randint(0,len(colors)-1)])
    
    def mode_enable(self,flag):
        if flag:
            self.configure(state=ctk.NORMAL)
        else:
            self.configure(state=ctk.DISABLED)
#----------------TILE_BUTTON--------------------#













