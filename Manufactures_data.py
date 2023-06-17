#!/usr/bin/env python
# coding: utf-8

# # Manufacturing Companies Data Analysis

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
get_ipython().run_line_magic('matplotlib', 'inline')
import scipy.stats as stats
sns.set_style('darkgrid')
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


# In[2]:


#uploading our dataframe to our work space
manu_data=pd.read_excel('Manufactures data.xlsx')

#loading sample of of our data frame
manu_data.head(10)


# In[3]:


#checking the size of our dataframe
manu_data.shape          


# In[4]:


#lets do location count
locat_count=manu_data['Location'].value_counts()
locat_count


# In[5]:


#lets present the above result in a pie chat
manu_data[manu_data['Location'].notnull()]['Location'].value_counts().plot(kind = 'pie', autopct='%1.1f%%', figsize=(8, 8))
plt.title('Manufacturers town locations')


# In[6]:


#lets find the count of different companies products
product_count=manu_data['Products'].value_counts()
product_count


# In[7]:


#lets see its presentation in a bar graph
prd_plot =product_count.plot.bar(x='Products', y='count', rot=90, figsize=(10,8))


# In[8]:


#let find kind of sevice offered by the differnt companies based of their products
prod_service=manu_data.groupby('Products')['Service_offered'].value_counts().sort_values(ascending=False)
prod_service


# In[9]:


manu_data.groupby('Products')['Service_offered'].value_counts().plot(kind='pie', y='Service_offered',
                                                                     autopct='%1.1f%%',figsize=(8,8))


# In[10]:


#lets get the count of the different servixe offered
Service_offered=manu_data['Service_offered'].value_counts()
Service_offered


# In[11]:


#lets see the result in a bar gragh
Service_offered.plot(kind ='bar',title='Service offered by Manufacturing companies ',x='Service_offered', y='count', 
                     figsize= (5,5))


# In[12]:


#lets find the trend in the challenges the manufacturing companies faced
challenge=manu_data['Challenge'].value_counts()
challenge


# In[13]:


#lets find the most common challenge
df1=manu_data.Challenge.str.split('/')
df1 = df1.explode('Challenge').value_counts()
df1


# In[14]:


#let check the distribution on a bar graph
df1.plot(kind ='bar',title='challenges Manufacturing companies faced',x='challenges', y='count', figsize= (15,5))


# In[ ]:




