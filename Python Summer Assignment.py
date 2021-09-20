#!/usr/bin/env python
# coding: utf-8

# In[5]:





# In[8]:


import pandas
newusers=pandas.read_csv(r'/Users/qmr/Desktop/semester1/APP/NewUsers.csv')
newusers


# In[27]:


ratingsinput=pandas.read_csv(r'/Users/qmr/Desktop/semester1/APP/RatingsInput.csv')
ratingsinput.head()


# In[28]:


ratingsinput
MovieName = ratingsinput["MovieName"]


# In[31]:


##task1
ratingsinput["MovieID"] = ratingsinput["MovieName"].str.split(",").str.get(0)
ratingsinput["MovieID"]


# In[34]:


ratingsinput["MovieName"] = ratingsinput["MovieName"].str.split(",").str.get(1)
ratingsinput["MovieName"]


# In[41]:


ratingsinput.to_csv(r'/Users/qmr/Desktop/semester1/APP/RatingsInput_task1.csv')


# In[50]:


##task2
##upper：every character
##capitalize: only for the first character of this sentence
##title: every first character of a word
ratingsinput["MovieName"] = ratingsinput["MovieName"].str.title()


# In[51]:


ratingsinput.to_csv(r'/Users/qmr/Desktop/semester1/APP/RatingsInput_task2.csv')


# In[98]:


#task3, take age as key and other as value
#step1, create an internal dict for rating and movie name
##collections counter for adding ints together
#dict.setdefault(kw, 0) # 默认值设为0
#dict.setdefault(kw, []) # 默认值为空列表
#dict.setdefault(kw, []).append(value) # 把value增加到kw对应的键值列表中，实现了一对多
#dict.setdefault(kw, {}) # 默认值为空字典 # 可实现字典嵌套
ri=pandas.read_csv(r'/Users/qmr/Desktop/semester1/APP/RatingsInput_task2.csv')
for 
ratings_dict = dict(zip(ri.Rating, ri.MovieName))
ratings_dict


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




