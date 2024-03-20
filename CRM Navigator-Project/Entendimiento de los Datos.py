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
#cust_clean = customers

