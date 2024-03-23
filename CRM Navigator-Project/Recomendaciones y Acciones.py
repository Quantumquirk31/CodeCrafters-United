import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame de pandas
df = pd.read_csv('Customers.csv')

# Calcular el ingreso mensual
df['Ingreso Mensual'] = df['Annual Income ($)'] / 12

# Calcular el gasto mensual total
df['Gasto Mensual Total'] = df['Work Experience'] * 1000 + df['Family Size'] * 500

# Calcular el porcentaje de ahorro
df['Porcentaje de Ahorro'] = ((df['Ingreso Mensual'] - df['Gasto Mensual Total']) / df['Ingreso Mensual']) * 100

# Visualizar los resultados
print(df[['CustomerID', 'Ingreso Mensual', 'Gasto Mensual Total', 'Porcentaje de Ahorro']])

# Gráfico de barras para visualizar el porcentaje de ahorro
plt.figure(figsize=(10, 6))
plt.bar(df['CustomerID'], df['Porcentaje de Ahorro'], color='skyblue')
plt.xlabel('CustomerID')
plt.ylabel('Porcentaje de Ahorro')
plt.title('Porcentaje de Ahorro por Cliente')
plt.xticks(df['CustomerID'])
plt.show()

#El objetivo es ya que cada cliente posee un presupuesto diferente, 
#hacer un plan de ahorro que sea el mas adecuado y que vaya acorde con su presupuesto mensual

