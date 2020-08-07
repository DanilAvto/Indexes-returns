#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[9]:


tickers = ['^GSPC','^IXIC','^GDAXI']

ind_data = pd.DataFrame()

for t in tickers:
    ind_data[t] = wb.DataReader(t, data_source = 'yahoo', start = '1997-1-1')['Adj Close']


# In[10]:


ind_data.head()


# In[11]:


ind_data.tail()


# In[18]:


(ind_data/ind_data.iloc[0]* 100).plot(figsize = (15, 8))
plt.show()


# In[19]:


ind_return = (ind_data/ind_data.shift(1)) - 1
print(ind_return)


# In[20]:


annual_ind_return = ind_return.mean() * 250
print(annual_ind_return)


# In[29]:


tickers = ['PG', '^GSPC','^GDAXI']
data2 = pd.DataFrame()
    
for t in tickers:
    data2[t] = wb.DataReader(t, data_source ='yahoo', start = '1997-1-1')['Adj Close']


# In[32]:


data2.head()


# In[36]:


(data2/data2.iloc[0]*100).plot(figsize = (15,6))


# In[ ]:




