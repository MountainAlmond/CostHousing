import pandas as pd

init_data = []
data_change = []
normal_data= []
init_data_frame = pd.DataFrame()
regress_data_frame = pd.DataFrame()
normal_data_frame = pd.DataFrame()
correlation_data_frame = pd.DataFrame()
pair_correl_matrix =[[]]
personal_correl_matrix =[[]]
koefs_regression = []
regression_df_final = pd.DataFrame()
HEADER_ROW = []
HEADER_COL = []
GO_CORREL = True
parametres_data = []

# #Delete header for operation with array of data
def del_header(data):
    data_prepared = data[:]
    data_prepared = [[col[1] for col in enumerate(row[1]) if col[0] != 0] for row in enumerate(data_prepared) if row[0] != 0]
    return data_prepared
#Header array data layout (empty header)
def column(matrix, i):
    return [row[i] for row in matrix]
def prepare_dataframe(init_frame):
    df = init_frame.drop([0])
    return df 