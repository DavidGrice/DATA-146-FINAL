
# coding: utf-8

# In[1]:


# Prakrit Shukla and David Grice

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as ss
import random
import math


# In[118]:


def OR_CI(a,b,c,d,alpha):
    est = math.log(a*d/(b*c))
    stderr = ((1/a) + (1/b) + (1/c) + (1/d))**0.5
    z = ss.norm.ppf(1-alpha/2)
    low = est - z*stderr
    high = est + z*stderr
    return math.e**low, math.e**high


# In[65]:


# First 13 questions dealing with Earthquake
earthQuake = pd.read_csv("earth_orig_dropped.csv")


# In[66]:


new_earthQuake = earthQuake[["Worried", "Worried_Big_One", "Big_One_Lifetime", "Preparations"]]
new_earthQuake


# In[67]:


new_earthQuake["Worried"]


# In[68]:


earthQuake


# In[69]:


earthQuake["Region"].describe()


# In[80]:


df = pd.DataFrame(earthQuake, columns=['Yellowstone', 'Worried_Big_One'])
#df=pandas.DataFrame(data, columns=['Fruit', 'Shop', 'Price'])
#df.pivot(index='Yellowstone', columns='Worried_Big_One')


# In[115]:


#table_1 = pd.crosstab(earthQuake["Yellowstone"], earthQuake["Woried_Big_One"])
table_1 = pd.crosstab(earthQuake['Yellowstone'], earthQuake['Worried_Big_One'])

columnsTitles = (['Not at all worried','Not so worried','Somewhat worried','Very worried','Extremely worried'])
table_1 = table_1.reindex(['Extremely familiar','Very familiar','Somewhat familiar','Not so familiar', 'Not at all familiar'], columns = columnsTitles)
#df.reindex(columns=columnsTitles)
table_1


# In[117]:


sns.heatmap(table_1, annot = True, cmap = 'BuPu')
#xticklabels=['Not at all worried','Not so worried','Somewhat worried',\
#                                                'Very worried','Extremely worried'], yticklabels=['Extremely familiar','Very familiar','Somewhat familiar','Not so familiar', 'Not at all familiar']
plt.xticks(rotation = 45)


# In[9]:


ss.contingency.chi2_contingency(table_1)


# In[10]:


# Question 11
table_2 = pd.crosstab(earthQuake['Preparations'], earthQuake['Big_One_Lifetime'])
table_2


# In[119]:


table_2_est = (488*140)/(278*72)
print(table_2_est)


# In[11]:


# Question 14 -> 18 dealing with Drugs
drugs = pd.read_csv("Drugs.txt", sep="\t")


# In[12]:


drugs.head()


# In[13]:


alcopiod = drugs[["Alcohol", "Opiods"]]


# In[14]:


alcopiod


# In[120]:


t = pd.crosstab(drugs.Alcohol,drugs.Opiods, margins=False)
t = t.sort_index(axis = 1, ascending=True)
t


# In[17]:


est = (7*16)/(20*3)
print(est)


# In[122]:


OR_CI(16,3,20,7,0.01)


# In[19]:


drugs2 = drugs[["Alcohol", "Marijuana"]]


# In[20]:


t2 = pd.crosstab(drugs2.Marijuana,drugs2.Alcohol, margins=False)
t2 = t2.sort_index(axis = 1, ascending=True)
t2


# In[21]:


ss.fisher_exact(t2)


# In[22]:


drug3 = drugs[["Opiods", "Marijuana"]]


# In[23]:


drug3


# In[24]:


t3 = pd.crosstab(drug3.Marijuana,drug3.Opiods, margins=False)
t3 = t3.sort_values(by=['Opiods','YES'], axis=1, ascending=True)
t3
# categorical / sort values


# In[123]:


ss.fisher_exact(t3)


# In[126]:


OR_CI(32,8,4,2,0.05)


# In[125]:


est3 = (32*2)/(8*4)
print(est3)


# In[28]:


# 17->20
OR_CI(20,18,25,137,0.05)


# In[29]:


n = [(20, 18),(25,137)]


# In[30]:


n


# In[31]:


i = (20/38)/(25/162)
i


# In[32]:


esti = (20*137)/(18*25)
print(esti)

