import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar el archivo CSV
df = pd.read_csv('mundo_ideal_karcal.csv')

# Supongamos que queremos predecir el 'Precio' basado en 'Monto de Garantía' y 'Pago del Restante'
# Asegúrate de reemplazar 'Precio' por la columna correspondiente en tu archivo CSV
X = df[['Monto de Garantía', 'Pago del Restante']]
y = df['Precio']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Error cuadrático medio: {mse}')
