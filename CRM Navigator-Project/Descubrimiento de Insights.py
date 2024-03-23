import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV
data = pd.read_csv('Customers.csv')

# Visualizar distribuciones de variables numéricas mediante histogramas
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
sns.histplot(data['Age'], kde=True, color='skyblue', bins=20)
plt.title('Distribución de Edades')

plt.subplot(2, 2, 2)
sns.histplot(data['Annual Income ($)'], kde=True, color='salmon', bins=20)
plt.title('Distribución de Ingresos Anuales')

plt.subplot(2, 2, 3)
sns.histplot(data['Spending Score (1-100)'], kde=True, color='green', bins=20)
plt.title('Distribución de Puntuación de Gasto')

plt.subplot(2, 2, 4)
sns.histplot(data['Work Experience'], kde=True, color='orange', bins=20)
plt.title('Distribución de Experiencia Laboral')

plt.tight_layout()
plt.show()

# Visualizar distribución de variables categóricas mediante diagramas de barras
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.countplot(x='Gender', data=data)
plt.title('Distribución de Género')

plt.subplot(1, 2, 2)
sns.countplot(x='Profession', data=data)
plt.title('Distribución de Profesión')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Eliminar columnas no numéricas
data_numeric = data.select_dtypes(include=['int64', 'float64'])

# Calcular matriz de correlación
correlation_matrix = data_numeric.corr()

# Visualizar matriz de correlación como un mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlación')
plt.show()

# Calcular estadísticas descriptivas para las variables numéricas
stats_descriptivas = data_numeric.describe()
