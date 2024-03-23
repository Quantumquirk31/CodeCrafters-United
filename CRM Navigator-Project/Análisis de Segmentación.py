import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import silhouette_score 

# Cargar los datos
data = pd.read_csv("Customers.csv")  # Ajustar la ruta según la estructura de tu directorio
data.head()  # Mostrar las primeras filas para asegurarse de que la carga de datos sea exitosa

# Extraer características relevantes
J = data[['Age','Annual Income ($)','Spending Score (1-100)']] 

# Estandarizar las características
scaler = StandardScaler() 
J_scaled = scaler.fit_transform(J)  

# Determinar el número óptimo de clústeres utilizando el método del codo
wcss = []
for i in range(1, 11): 
    kmeans = KMeans(n_clusters=i, max_iter=50, random_state=0)
    kmeans.fit(J_scaled)
    wcss.append(kmeans.inertia_)

# Graficar la curva del codo
plt.figure(figsize=(10, 8)) 
plt.plot(range(1, 11), wcss)
plt.title("Método del Codo para K Óptimo")
plt.xlabel("Número de Clústeres")
plt.ylabel('WCSS')
plt.show()

# Realizar el clustering KMeans con el número óptimo de clústeres
kmeans = KMeans(n_clusters=6, init='k-means++', n_init=10, random_state=35)
data['Cluster'] = kmeans.fit_predict(J_scaled)

# Visualizar los clústeres
plt.figure(figsize=(10, 6))
plt.scatter(J['Annual Income ($)'], J['Spending Score (1-100)'], c=data['Cluster'], cmap='tab20')
plt.title("Segmentación de Clientes")
plt.xlabel("Ingreso Anual")
plt.ylabel("Gasto (1-100)")
plt.show()

