import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer el archivo CSV
customers = pd.read_csv('Customers.csv')
custumers.head(5)

# Descripción de Datos
def data_description(customers, head=5):
  print("FORMA: ".center(70, '-'))
  print("Filas: {}".format(customers.shape[0]))
  print("Columnas: {}".format(costumers.shape[1]))
  print("TIPOS: ".center(70, '-'))
  print(customers.dtypes)
  print("HEAD: ".center(70, '-'))
  printt(customers.head(head))
  print("TAIL: ".center(70, '-'))
  print(costumers.tail(head))
  print("VALORES NULOS: ".center(70, '-'))
  print(customers.isnull().sum())
  print("VALORES DUPLICADOS: ".center(70, '-'))
  print(customers.duplicated().sum())
  print("QUIANTILES: ".center(70, '-'))
  print(customers.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

data_description(customers)

# Limpieza de datos

cust_clean= customers.dropna()
print("El total de datos después de remover los vacíos es de:", len(cust_clean))

# Visualización de los datos

  # Gráfico de barras para distribución de género
gender = cust_clean['Gender'].valuecounts().reset_index()
gender.columns = ['Gender', 'Count']
plt.figure(figsize=(8, 6))
plt.pie(gender, labels=gender.idex, autopct='%1.1f%%', startangle=90, colors['skyblue', 'pink'])
plt.title('Gender Distribution')
plt.axis('equal') 
plt.show()

  # Gráficos de historiograma para valores numéricos
sns.set(style='whitegrid')
plt.figure(figsize=(15, 8))
for i, col in enumerate(['Age', 'Annual Income ($)', 'Spending Score (1-100)', 'Work Experience', 'Family Size'], start=1):
    plt.subplot(2, 3, i)
    sns.histplot(data[col], bins=20, kde=True)
    plt.title(f'Distribution of {col}')

plt.tight_layout()
plt.show()

  # Gráficos de barras para categorías
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.countplot(x='Gender', cust_clean=cust_clean)
plt.title('Recuento de Clientes por Profesión')
plt.tight_layout()
plt.show()
