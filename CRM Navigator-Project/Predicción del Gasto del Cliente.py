import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Leer el archivo CSV
customers_df = pd.read_csv('Customers.csv')

# Codificar variables categóricas
customers_df_encoded = pd.get_dummies(customers_df, columns=['Profession'], drop_first=True, prefix='Profession')

# Seleccionar características y variable objetivo
X = customers_df_encoded[['Annual Income ($)', 'Age', 'Profession_Healthcare', 'Work Experience', 'Family Size']]
y = customers_df_encoded['Spending Score (1-100)']

# Paso 1: Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 2: Entrenar un modelo de regresión para predecir el gasto del cliente
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

# Paso 3: Evaluar el rendimiento del modelo utilizando métricas de regresión
y_pred = regression_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean Squared Error:', mse)
print('R^2 Score:', r2)

# Visualizar la predicción del gasto del cliente
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.title('Predicción del Gasto del Cliente')
plt.xlabel('Gasto Real del Cliente')
plt.ylabel('Predicción del Gasto del Cliente')
plt.show()

