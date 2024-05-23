import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from customtkinter import *
from tkinter.ttk import *
import scipy.stats as sps
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.interpolate import interp1d
import constants as const
import statistic


matplotlib.use("TkAgg")


def analyze_distr(master,data):
    plot = plt.figure(figsize=(4, 3))
    plt.title(r"Сравнение распределения с нормальным")
    plt.axis('off') 
    sns.distplot(data, rug=False, fit=sps.norm, color='red',hist=False, label='Действительное распределение')
    canvas = FigureCanvasTkAgg(plot, master)
    canvas.get_tk_widget().grid(row=0, column=0)
    plt.legend(loc='upper left')

matplotlib.use("TkAgg")


def analyze_distr(master,data):
    plot = plt.figure(figsize=(7, 5))
    plt.title(r"Сравнение распределения с нормальным")
    plt.axis('off') 
    sns.distplot(data, rug=False, fit=sps.norm, color='red',hist=False, label='Действительное распределение')
    canvas = FigureCanvasTkAgg(plot, master)
    canvas.get_tk_widget().pack()
    plt.legend(loc='upper left')

def interval_mark(master,x,y):
    #cubic_interpolation_model = interp1d(x, y, kind = "cubic")
    #X_=np.linspace(min(x), max(x), 500)
    #Y_=cubic_interpolation_model(X_)
    plot = plt.figure(figsize=(7, 5))
    plt.plot(x, y)
    # plt.hist(weights=y,bins=[0,0.2,0.4,0.6,0.8], width=0.2)
    
    plt.hist(weights=y,bins=[0,0.2,0.4,0.6,0.8,1],x=x)
    plt.title("Гистограмма распределения")
    plt.xlabel("Интервалы")
    plt.ylabel("Кол-во элементов, попавших в интервал")
    canvas = FigureCanvasTkAgg(plot, master)
    canvas.get_tk_widget().pack()
    
def correlation_matrix(master,df):
    plot = plt.figure(figsize=(12,10), dpi= 80)
    sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)

    # Decorations
    plt.title('Матрица корреляций', fontsize=22)
    plt.xticks(fontsize=12)
    
    plt.yticks(fontsize=12)
    canvas = FigureCanvasTkAgg(plot, master)
    canvas.get_tk_widget().pack()

def mark_regression(master,regression,real):
    plot = plt.figure(figsize=(12,10), dpi= 80)
    # mapping = list(range(const.DATA_LENGTH))
    plt.title('Поведение графика регрессии', fontsize=22)
    # reg_smoothed = gaussian_filter1d(regression, sigma=2)
    # real_smoothed = gaussian_filter1d(real, sigma=2)
    plt.plot(regression,label='Регрессия')
    plt.plot(real,label='Действ. значения')
    plt.legend()
    canvas = FigureCanvasTkAgg(plot, master)
    # canvas.get_tk_widget().pack(side=TOP)
    canvas.get_tk_widget().grid(column=0,row=0,padx=5,pady=5)
# plot()

    














 
