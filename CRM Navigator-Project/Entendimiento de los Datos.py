import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer el archivo CSV
customers = pd.read_csv('Customers.csv')
customers.head(5)

# Descripción de Datos
def data_description(customers, head=5):
    print("-" * 70)
    print("TAMAÑO:".center(70))
    print("Filas:", customers.shape[0])
    print("Columnas:", customers.shape[1])
    print("-" * 70)
    print("TIPOS:".center(70))
    print(customers.dtypes)
    print("-" * 70)
    print("HEAD:".center(70))
    print(customers.head(head))
    print("-" * 70)
    print("TAIL:".center(70))
    print(customers.tail(head))
    print("-" * 70)
    print("VALORES NULOS:".center(70))
    print(customers.isnull().sum())
    print("-" * 70)
    print("VALORES DUPLICADOS:".center(70))
    print(customers.duplicated().sum())
    print("-" * 70)

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
