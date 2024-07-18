import plotly.express as px

# Datos de prueba
df = px.data.iris()

# Crear un gráfico de dispersión simple
fig = px.scatter(df, x='sepal_width', y='sepal_length')

# Mostrar el gráfico
fig.show()
