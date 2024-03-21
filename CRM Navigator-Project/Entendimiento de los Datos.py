import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tabulate import tabulate
from IPython.display import display, HTML

# Leer el archivo CSV
customers = pd.read_csv('Customers.csv')
customers.head(5)

# Descripción de Datos
def data_description(customers, head=5):
    display(HTML("<h3 style='text-align:center;'>TAMAÑO:</h3>"))
    display(customers.shape)
    
    display(HTML("<h3 style='text-align:center;'>TIPOS:</h3>"))
    display(customers.dtypes.to_frame().reset_index().rename(columns={'index': 'Columna', 0: 'Tipo'}))
    
    display(HTML("<h3 style='text-align:center;'>HEAD:</h3>"))
    display(customers.head(head))
    
    display(HTML("<h3 style='text-align:center;'>TAIL:</h3>"))
    display(customers.tail(head))
    
    display(HTML("<h3 style='text-align:center;'>VALORES NULOS:</h3>"))
    display(customers.isnull().sum().to_frame().reset_index().rename(columns={'index': 'Columna', 0: 'Valores Nulos'}))
    
    display(HTML("<h3 style='text-align:center;'>VALORES DUPLICADOS:</h3>"))
    display(customers.duplicated().sum())

data_description(customers)

# Limpieza de datos
cust_clean = customers.dropna()
print("El total de datos después de remover los vacíos es de:", len(cust_clean))

# Visualización de los datos

# Gráfico de barras para distribución de género
gender = cust_clean['Gender'].value_counts().reset_index()
gender.columns = ['Gender', 'Count']
colors = ['pink', 'skyblue']
plt.figure(figsize=(8, 6))
plt.pie(gender['Count'], labels=gender['Gender'], autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Gender Distribution')
plt.axis('equal')
plt.show()

# Gráficos de historiograma para valores numéricos
sns.set(style='whitegrid')
plt.figure(figsize=(15, 8))
for i, col in enumerate(['Age', 'Annual Income ($)', 'Spending Score (1-100)', 'Work Experience', 'Family Size'], start=1):
    plt.subplot(2, 3, i)
    sns.histplot(cust_clean[col], bins=20, kde=True)
    plt.title(f'Distribution of {col}')

plt.tight_layout()
plt.show()

# Gráficos de barras para categorías
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.countplot(x='Gender', data=cust_clean)
plt.title('Recuento de Clientes por Género')
plt.subplot(1, 2, 2)
sns.countplot(y='Profession', data=cust_clean)
plt.title('Count of Customers by Profession')

plt.tight_layout()
plt.show()

