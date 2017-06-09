
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:xx

    #this does the same thing as the below shell but with fewer lines 
with open('dmv504n00.mmd.as.cn.co2.nl.mo.dat','r') as f:
    x_axis = 'DATE'
    y_axis = 'CO2'
    yeet = list(range(22))
    yeet[0] = x_axis
    yeet[4] = y_axis
        
    df = pd.DataFrame((l.rstrip().split() for l in f), columns=yeet)

    copy_a_df = df.copy()
    copy_a_df = copy_a_df.drop(df.index[range(0,37)])    ##remove unnessary columns and rows
    copy_a_df = copy_a_df.drop(df.index[range(1,4)], axis=1)
    copy_a_df = copy_a_df.drop(df.index[range(5,7)], axis=1)
    copy_a_df = copy_a_df.drop(df.index[range(7,10)], axis=1)
    copy_a_df = copy_a_df.drop(df.index[10], axis=1)
    


# In[ ]:

    #here I will attempt to plot this data in a scatterplot
copy_c_df = copy_a_df.copy()
copy_c_df = copy_c_df.T
copy_c_df = copy_c_df.drop(df.index[range(11,22)], axis=0)  #remove unnecessary column
copy_c_df = copy_c_df.T
copy_c_df = copy_c_df.drop(df.index[37])
#copy_c_df = copy_c_df.T   #comment this out to plot


copy_d_df = copy_c_df.copy()

copy_d_df[x_axis] = pd.to_numeric(copy_d_df[x_axis], errors = 'coerce')
#copy_d_df = copy_d_df.T
copy_e_df = copy_d_df.copy()

#print(copy_d_df.index)

copy_e_df[[x_axis, y_axis]].set_index(x_axis).plot(figsize=(15,8))  #uncommented when above is commented out  #doesn't reach this
# In[]:
    