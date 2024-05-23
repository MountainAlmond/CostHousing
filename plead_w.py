import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import customtkinter as ctk
import networkx as nx
import numpy as np
from helpGUI_funcs import *
import data_global as Data
from constants import *
import copy

class plead_view(ctk.CTkToplevel):
    

    def __init__(self):
        super().__init__()
        self.title("Корреляционные плеяды")
        center_window(self,1)
        ctk.set_default_color_theme("green")
        f = plt.figure(figsize=(20, 20))
        canvas = FigureCanvasTkAgg(f, master=self)
        
        def build_graph_correl(root,matrix):
            # matrix = copy.deepcopy(Data.pair_correl_matrix)

            plt.axis('off')

            G = nx.Graph(directed = True)
            for i in range(len(Data.HEADER_ROW)):
                G.add_node(Data.HEADER_ROW[i])

            for i in range(len(Data.HEADER_ROW)):
                for j in range(len(Data.HEADER_ROW)):
                    if(i!=j):
                        if(abs(matrix[i][j])<0.3):
                            if(matrix[i][j]>0):
                                G.add_edge(Data.HEADER_ROW[i],Data.HEADER_ROW[j],color = 'green',weight=5)
                            else:
                                G.add_edge(Data.HEADER_ROW[i],Data.HEADER_ROW[j],color = 'green',weight=1)
                        if(abs(matrix[i][j])>=0.3 and abs(matrix[i][j])<=0.6):
                            if(matrix[i][j]>0):
                                G.add_edge(Data.HEADER_ROW[i],Data.HEADER_ROW[j],color = 'blue',weight=5)
                            else:
                                G.add_edge(Data.HEADER_ROW[i],Data.HEADER_ROW[j],color = 'blue',weight=1)
                        if(abs(matrix[i][j])>=0.6 and abs(matrix[i][j])<=0.7):
                            if(matrix[i][j]>0):
                                G.add_edge(Data.HEADER_ROW[i],Data.HEADER_ROW[j],color = 'orange',weight=5)
                            else:
                                G.add_edge(Data.HEADER_ROW[i],Data.HEADER_ROW[j],color = 'orange',weight=1)
                        if(abs(matrix[i][j])>0.7):
                            if(matrix[i][j]>0):
                                G.add_edge(Data.HEADER_ROW[i],Data.HEADER_ROW[j],color = 'red',weight=5)
                            else:
                                G.add_edge(Data.HEADER_ROW[i],Data.HEADER_ROW[j],color = 'red',weight=1)
                            

            edges,colors = zip(*nx.get_edge_attributes(G,'color').items())
            # nx.draw(G,edgelist=edges,edge_color=colors,width=10)

            weights = [G[u][v]['weight'] for u,v in edges]
            nx.draw_networkx(G,edgelist=edges,edge_color=colors, with_labels=True, node_size = 300, arrows = True,
                             pos=nx.circular_layout(G), width = weights)
            
        
           
            canvas.get_tk_widget().pack(side='bottom', fill='both', expand=1)

        
        btn_pair = ctk.CTkButton(master = self,text='Построить плеяду парных корреляций',
                                 command=lambda:build_graph_correl(self,Data.pair_correl_matrix))
        btn_personal = ctk.CTkButton(master = self,text='Построить плеяду частных корреляций',
                                     command=lambda:build_graph_correl(self,Data.personal_correl_matrix))
        btn_pair.pack()
        btn_personal.pack()
       
    


