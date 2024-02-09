#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


url = "https://webpages.charlotte.edu/mscipion/"

r = requests.get(url)
print(r)


# In[3]:


soup = BeautifulSoup(r.text, "lxml")


# In[4]:


table = soup.find("table")


# In[5]:


headers = table.find_all("th")


# In[9]:


titles = []

for i in headers:
    title = i.text
    titles.append(title)
    
print(titles)


# In[10]:


df = pd.DataFrame(columns=titles)


# In[11]:


rows = table.find_all("tr")
for i in rows[1:]:
    print(i)


# In[12]:


for i in rows[1:]:
    
    data = table.find_all("td")
    row = [tr.text for tr in data]


# In[13]:


rows[1:2]


# In[14]:


for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    l = len(df)
    df.loc[l] = row
    
df.head(10)


# In[ ]:




