#!/usr/bin/env python
# coding: utf-8

# COVID-19 TRACKING
# 

# In[1]:


import pandas as pd
df=pd.read_json('https://www.mohfw.gov.in/data/datanew.json')
df


# In[2]:


df=df.iloc[:-1,1:]


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
total_states=np.arange(len(df['state_name']))


# In[6]:


total_states


# In[7]:


df['active']


# In[9]:


max(df['positive'])


# In[11]:


###Total Positive Cases based on states in India
from matplotlib.pyplot import figure
figure(num=None, figsize=(9,6),dpi=80,facecolor='w',edgecolor='k')
plt.barh(total_states,df['positive'],align='center',alpha=0.5,color=(1,0,0),edgecolor=(0.5,0.2,0.8))
plt.yticks(total_states,df['state_name'])
plt.xlim(1,max(df['positive'])+10)
plt.xlabel('Positive Number of Cases')
plt.title('Corona Virus Cases')
plt.show()


# In[12]:


##Active Number of Cases based on States
from matplotlib.pyplot import figure
figure(num=None,figsize=(9,6),dpi=80,facecolor='w',edgecolor='k')
plt.barh(total_states,df['active'],align='center',alpha=0.5,color=(1,0.5,0),edgecolor=(0.5,0.4,0.8))
plt.yticks(total_states,df['state_name'])
plt.xlim(1,max(df['active'])+10)
plt.xlabel('Active number of cases')
plt.title('Corona Virus Cases')
plt.show()


# In[15]:


##Death number of cases
from matplotlib.pyplot import figure
figure(num=None,figsize=(9,6),dpi=80,facecolor='w',edgecolor='k')
plt.barh(total_states,df['death'],align='center',alpha=0.5,color=(0,0,1),edgecolor=(0.5,0.4,0.8))
plt.yticks(total_states,df['state_name'])
plt.xlim(1,max(df['death'])+10)
plt.xlabel('Death number of cases')
plt.title('Corona Virus Cases')
plt.show()


# In[16]:


###Stack all the columns in th barchart
df.columns


# In[18]:


df=df.set_index('state_name',drop=True)


# In[19]:


df.head()


# In[20]:


###Plotting Based on Stacking
df.plot.barh(stacked=True,figsize=(15,15))


# In[ ]:




