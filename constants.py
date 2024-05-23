colors = ['#03541e','#c9aa0a','#cc2702','#02cccc','#2b3699','#92279c','#ff001e']

colors_dict = {'green':'#04d13e',
               'cream':'#c2eb8d',
               'brown':'#8f5907',
               'beige':'#ffc670',
               'purple':'#8a3051',
               'dark_orange':'#a13c2f',
               'mute_yellow':'#ed9a1c'
    
}


filetypes = [
        ('Excel files', '*.XLSX')
        # ('All files', '*.*')
]

HEAD_COL_PARAM = ["Параметры","Ср.арифм.","Мода", "Медиана","Стандартное отклонение","Дисперсия", "Эксцесс",
             "Коэф.вариации","Коэф. асимметрии","Минимум", "Максимум","Количество элементов"]

index_variance = 5
        
HEAD_COL_ERROR = ["", "Средняя ошибка", "Предельная ошибка", "Необходимый объем выборки"]

HEAD_COL_MARK_NORMAL = ["","Хи-квадрат",'Предельное значение','Распределение по интервалам','Границы интервалов', "Нормальность"]

HEAD_COL_REGRESSION = ["Коэф.", "Название коэфф-а", "Значение коэфф-а"]

HEAD_COL_REGRESSION_FINAL = ["R-квадрат", "F-критерий","Крит. F-критерий", "Количество наблюдений"]


CRITICAL_PROBABILITY = 0.05

CRITICAL_PIRSON = 30.1

CRITICAL_STUDENT = 2.09

CRITICAL_FISHER = 2.85

VALUE_STEP = 5

DATA_LENGTH = 21

path_wallpaper_image = r'images\wallpaper.jpg'
path_normal_image = r'images\normal.png'
path_parametres_image=r'images\parametrs.png'
path_normal_mark_image=r'images\mark_normal.png'
path_correlation_image = r'images\correlation.jpg'
path_plead_image = r'images\plead.png'
path_regression_image = r'images\regression.png'
path_about_text = r'info\readme.txt'

HEADER_PLEAD = ['x0','x1','x2','x3','x4','x5','x6','x7']