import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer el archivo CSV
customers_df = pd.read_csv('Customers.csv')

# Codificar columnas categóricas usando one-hot encoding
customers_df_encoded = pd.get_dummies(customers_df)

# Eliminar la columna 'CustomerID' si es necesario
if 'CustomerID' in customers_df_encoded:
    customers_df_encoded = customers_df_encoded.drop(columns=['CustomerID'])

# Calcular la matriz de correlación
correlation_matrix = customers_df_encoded.corr()

# Visualizar la matriz de correlación utilizando un mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
plt.title('Matriz de Correlación')
plt.show()

