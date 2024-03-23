#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import silhouette_score 


# In[62]:


data = pd.read_csv(r"C:\Users\moral\OneDrive\Escritorio\Customers.csv")  
variable.head() 


# In[63]:


J =data[['Age','Annual Income ($)','Spending Score (1-100)']] 


# In[64]:


data.describe()


# In[65]:


scaler = StandardScaler() 
J_scaled = scaler.fit_transform(J)  


# In[66]:


data.describe() 


# In[77]:


wcss = []

for i in range (1,11): 
    kmeans= KMeans(n_clusters = i, max_iter= 50)
    kmeans.fit(J_scaled)
    wcss.append(kmeans.inertia_)


# In[81]:


plt.figure(figsize=(10, 8)) 
plt.plot(range(1,11), wcss)
plt.title("Codo Customers") 
plt.xlabel("Numero de clusters")
plt.ylabel('WCSS')
plt.show()


# In[94]:


kmeans = KMeans(n_clusters=6, init='k-means++', n_init=10, random_state=35)
data['Cluster'] = kmeans.fit_predict(J_scaled)

plt.figure(figsize=(10, 6))
plt.scatter(J['Annual Income ($)'], J['Spending Score (1-100)'], c=data['Cluster'], cmap='tab20')
plt.title("Segmentacion de Clientes")
plt.xlabel("Ingreso Anual")
plt.ylabel("Gasto (1-100)")
plt.show() 


# In[ ]:




