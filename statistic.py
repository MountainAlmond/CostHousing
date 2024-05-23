import pandas as pd
import numpy as np
import data_global as Data
from collections import Counter
from math import sqrt
#asymmetry
from scipy.stats import skew
#excess
from scipy.stats import kurtosis
import constants as const
import data_global as Data
from statistics import mode
def min_max_norm(data):
    df = pd.DataFrame(data)
    
    normalized_df=(df-df.min())/(df.max()-df.min())
    normalized_df.index = Data.HEADER_COL
    normalized_df.columns = Data.HEADER_ROW
    normalized_df.insert(0, "ГОД", Data.HEADER_COL)
    normalized_df = normalized_df.round(2)
    normalized_df['ГОД'] = normalized_df['ГОД'].astype(str)
    
    
    Data.normal_data = [normalized_df.columns.values.tolist()] + normalized_df.values.tolist()
    normalized_df.drop('ГОД', axis=1,inplace=True)
    Data.normal_data_frame = normalized_df



def variance(observations):
    mean = sum(observations) / len(observations)
    squared_differences = 0
    for number in observations:
        difference = mean - number
        squared_difference = difference ** 2
        squared_differences += squared_difference
    variance = squared_differences / (len(observations) - 1)
    
    return variance

def std_dev(observation_input):
    return sqrt(variance(observations=observation_input))
    

def mean(observations):
    return sum(observations) / len(observations)

# def mode(observations):
#     c = Counter(observations) 
#     return [k for k, v in c.items() if v == c.most_common(1)[0][1]]


def median(observations): 
    return max(set(observations), key=observations.count) 

def CV(observations_):
    return (std_dev(observation_input=observations_)/mean(observations=observations_))*100

    
def Xi_square(wait_data,emp_data):
    if len(wait_data) != len(emp_data):
        raise Exception('Lens is not equal')
    Xi_value = 0
    for i in range(len(wait_data)):
        Xi_value = Xi_value + (emp_data[i]-wait_data[i])**2/wait_data[i]
    return Xi_value

func_list = [mean,mode,median,std_dev,variance,kurtosis,CV,skew,min,max,len]


def interval_series(observations):
    step_value = (max(observations)-min(observations)) / const.VALUE_STEP
    observations.sort()
    result = []
    current_right_border = min(observations)+step_value
   
    current_item = 0
    counter = 0
    for i in range(const.VALUE_STEP):
        while (current_item < len(observations) and observations[current_item]<=current_right_border):
            current_item = current_item + 1
            counter = counter + 1
        result.append(counter)
        counter = 0
        current_right_border = current_right_border + step_value
    return result

def lst_to_str(lst,sep):
    s = sep.join(str(x) for x in lst)
    return s

def get_borders(observations):
    step_value = round((max(observations)-min(observations)) / const.VALUE_STEP,3)
    res = []
    res.append(0)
    current_right_border = min(observations)+step_value
    for i in range(const.VALUE_STEP):
        res.append(current_right_border)
        current_right_border = round(current_right_border + step_value,3)
    
    str_res = lst_to_str(res,' ')
    return str_res
def get_middle():
    return [0.1,0.3,0.5,0.7,0.9]


#-----------------CORRELATION BLOCK--------------------------#


#Get koef correlation between X1 X2 (Pirson koef)

##############################################################################
#For get koef correlation Pirson need:                                       #                   
#       --mean of X1 and X2                                                  #                                   
#       --X1-X1(mean) r_component1                                           #                               
#       --X2-X2(mean) r_component2                                           #
#       --(X1-X1(mean))^2  (1)  r_component3                                 #
#       --(X2-X2(mean))^2   (2) r_component4                                 #
#       --(X1-X1(mean)*(X2-X2(mean))) (3)  rcomponent5                       #
#                                                                            #
#                       !!!r=(3)/sqrt((1)*(2))!!!                            #
##############################################################################
    
    
def get_Pirson_correlation(X1,X2):
    if type(X1) is not list or type(X2) is not list:
        raise Exception("Observations must be type of list!")
    else:
        if len(X1)!=len(X2):
            raise Exception("Observations must be equal len!")
        else:
            # get means of X1 and X2
            X1_mean = mean(observations=X1)
            X2_mean = mean(observations=X2)
            #init components for koef correlation
            r_component1, r_component2, r_component3, r_component4,r_component5 = [],[],[],[],[]

            for i in range(len(X1)):
                val1 = X1[i]-X1_mean
                val2 = X2[i]-X2_mean
                r_component1.append(val1)
                r_component2.append(val2)
                r_component3.append(val1**2)
                r_component4.append(val2**2)
                r_component5.append(val1*val2)
            
            #calculate koef correlation of Pirson
            r = sum(r_component5) / sqrt(sum(r_component3)*sum(r_component4))

            return r

#getting the Student's significance level

##############################################################################
#For get koef Student's significance need:                                   #                   
#       --mean of X1 and X2  (1) and (2)                                     #
#       --std dev of X1 and X2  (3) and (4)                                  #                                   
#                                                                            #
#                                                                            #
#                       !!!t=(1)-(2)/(sqrt((3)+(4)))!!                       #
##############################################################################
def get_Student_pair_koef(r):       #was X1,X2
    # if type(X1) is not list or type(X2) is not list:
    #     raise Exception("Observations must be type of list!")
    # else:
    #     if len(X1)!=len(X2):
    #         raise Exception("Observations must be equal len!")
        # else:
            # get means of X1 and X2
            # X1_mean = mean(observations=X1)
            # X2_mean = mean(observations=X2)

            # #get std_dev of X1 and X2
            # X1_stdDev = std_dev(X1)
            # X2_stdDev = std_dev(X2)

            # #get the Student's significance level

            # t = (X1_mean - X2_mean) / (sqrt(X1_stdDev**2+X2_stdDev**2))
    t = abs(r)*sqrt((const.DATA_LENGTH-2)/(1-r**2))
    return t   

#-----------------CORRELATION BLOCK--------------------------#



def get_koef_regression(X,Y):
    if type(X) is not list or type(Y) is not list:
        raise Exception("Observations must be type of list!")
    else:
        if len(X)!=len(Y):
            raise Exception("Observations must be equal len!")
        else:
            sum_X = sum(X)
            sum_Y = sum(Y)

            xy = 0
            x_square = 0
            for i in range(len(X)):
                xy=xy+X[i]*Y[i]
                x_square = x_square + X[i]**2
            
            B = (const.DATA_LENGTH * xy - (sum_X*sum_Y))/(const.DATA_LENGTH*x_square-sum_X**2)
            B0 = (sum_Y - B * sum_X)/const.DATA_LENGTH

            return (B,B0)
            



#print(get_Student_pair_koef([0.2,0.7,0.5],[0.9,0.2,0.4]))
