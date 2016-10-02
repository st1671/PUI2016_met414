
# coding: utf-8

# In[6]:

from __future__  import print_function, division
import pylab as pl
import pandas as pd
import numpy as np
import os

get_ipython().magic('pylab inline')


# # Idea: Subscribers are more likely than non-subscribers (users) to use Citibikes Monday through Friday.
# 
# ## Null Hypothesis: Non-subscribers (users) use Citibikes as much or more than subscribers Monday through Friday.
# 
# ## Alternative Hypothsesis: Non-subscribers use Citibike less than subscribers Monday through Friday.
# 
# #### Significance Level $\\alpha=0.05$

# In[ ]:




# In[ ]:




# In[7]:

import zipfile

datestring = '201502'
get_ipython().system('curl -O "https://s3.amazonaws.com/tripdata/{datestring}-citibike-tripdata.zip"')

zf = zipfile.ZipFile(datestring+'-citibike-tripdata.zip')
df = pd.read_csv(zf.open(datestring+'-citibike-tripdata.csv'))

df['date'] = pd.to_datetime(df['starttime'])
df.head()


# In[8]:

df.columns


# In[17]:

data_reduct = df.drop(df.columns[[0,1,2,3,4,5,6,7,8,9,10,11,13,14]], axis =1)
data_reduct.head(79)


# In[18]:

df['usertype'] = df['usertype'].replace(['Subscriber','Customer'],[1,2])


# In[23]:

data_reduct = df.drop(df.columns[[0,1,2,3,4,5,6,7,8,9,10,11,13,14]], axis =1)
data_reduct.head(79)


# In[28]:

fig = pl.figure(figsize(15,15))

norm_w = 1
((df['date'][df['usertype'] == 2].groupby([df['date'].dt.weekday]).count()) / norm_w).plot(kind="bar", 
                                                                                         color='IndianRed', 
                                                                                         label='Non-Subscriber')

norm_m = 1
ax = ((df['date'][df['usertype'] == 1].groupby([df['date'].dt.weekday]).count()) / norm_m).plot(kind="bar", 
                                                                                              color='SteelBlue', 
                                                                                              alpha=0.5,
                                                                                              label='Subscriber')

tmp = ax.xaxis.set_ticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], fontsize=20)
ax.set_ylim([0,50000])
pl.xlabel('Day of The Week',fontsize=15)
pl.title("Daily Citibike Usage by User Type by Day of the Week, February 2015", fontsize=25)
pl.legend()


# # Daily Citibike Usage by User Type by Day of the Week, February 2015

# In[ ]:



