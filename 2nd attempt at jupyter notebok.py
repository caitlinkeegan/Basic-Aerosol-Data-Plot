
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:xx

with open('dmv504n00.mmd.as.cn.co2.nl.mo.dat','r') as f:
    #next(f) # skip first row
    yeet = list(range(22))
    yeet[0] = 'DATE'
    yeet[4] = 'CO2'
    df = pd.DataFrame((l.rstrip().split() for l in f), columns=yeet)
    
    copy_a_df = df.copy()
    copy_a_df = copy_a_df.drop(df.index[range(0,37)])    ##remove unnessary columns and rows
    copy_a_df = copy_a_df.drop(df.index[range(1,4)], axis=1)
    copy_a_df = copy_a_df.drop(df.index[range(5,7)], axis=1)
    copy_a_df = copy_a_df.drop(df.index[range(7,10)], axis=1)
    copy_a_df = copy_a_df.drop(df.index[10], axis=1)
    

# In[ ]:

copy_c_df = copy_a_df.copy()
copy_c_df = copy_c_df.T
copy_c_df = copy_c_df.drop(df.index[range(11,22)], axis=0)  #remove unnecessary column
copy_c_df = copy_c_df.T
copy_c_df = copy_c_df.drop(df.index[37])
#copy_c_df = copy_c_df.T   #comment this out to plot


#copy_c_df.loc['DATE'] = copy_c_df.loc['DATE'].apply(pd.to_numeric(date_list))
#copy_c_df.loc['CO2'] = copy_c_df.loc['CO2'].apply(pd.to_numeric(co2_list))
#copy_c_df.iloc[1] = copy_c_df.iloc[1].apply(pd.to_numeric)  #most recent

#copy_c_df = copy_c_df.T
copy_d_df = copy_c_df.copy()

copy_d_df['CO2'] = pd.to_numeric(copy_d_df['CO2'], errors = 'coerce')  #this converts from dtype:object to dtype:int64
print(copy_d_df.index)  #confirms that the conversion was successful
               

#copy_e_df = copy_e_df.copy()
#copy_d_df = copy_d_df.T
copy_e_df = copy_d_df.copy()

#print(copy_d_df.index)

copy_e_df[['DATE', 'CO2']].set_index('DATE').plot(figsize=(15,8))  #uncommented when above is commented out  
# In[]:
    
