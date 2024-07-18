import pandas as pd
import random
from faker import Faker
import datetime

fake = Faker('es_ES')
Faker.seed(0)

# Función para generar RUT chileno
def generate_rut():
    number = random.randint(1000000, 25000000)
    digits = list(map(int, str(number)))
    factors = [2, 3, 4, 5, 6, 7] * 3
    s = sum(d * f for d, f in zip(digits[::-1], factors))
    remainder = (-s) % 11
    if remainder == 10:
        remainder = 'K'
    return f"{number}-{remainder}"

# Datos ficticios
banks = ['Banco de Chile', 'Banco Estado', 'Santander', 'BCI', 'Scotiabank']
car_models = ['Toyota Corolla', 'Honda Civic', 'Ford Fiesta', 'Chevrolet Spark', 'Nissan Sentra']
car_categories = ['Sedán', 'Hatchback', 'SUV', 'Camioneta', 'Coupé']
auto_providers = ['Banco de Chile', 'Banco Estado', 'Santander', 'BCI', 'Scotiabank']
comunas = ['Santiago', 'Ñuñoa', 'Providencia', 'Las Condes', 'Vitacura', 'La Florida']

# Generar datos
data = []
for _ in range(1800):
    nombre = fake.first_name()
    apellido = fake.last_name()
    rut = generate_rut()
    direccion = fake.address()
    comuna = random.choice(comunas)
    cuenta_corriente = fake.iban()
    banco = random.choice(banks)
    monto_garantia = round(random.uniform(500000, 2000000), 2)
    fecha_pago_garantia = fake.date_this_year(before_today=True, after_today=False)
    n_jornada_remate = random.randint(1, 50)
    fecha_remate = fake.date_between(start_date=fecha_pago_garantia, end_date=datetime.date(2024, 12, 31))
    modelo_auto = random.choice(car_models)
    categoria_auto = random.choice(car_categories)
    proveedor_auto = random.choice(auto_providers)
    pago_restante = round(random.uniform(5000000, 20000000), 2) if random.random() > 0.5 else 0
    fecha_pago_restante = fake.date_between(start_date=fecha_remate, end_date=datetime.date(2024, 12, 31)) if pago_restante else None
    devolucion_garantia = monto_garantia if pago_restante == 0 else 0
    fecha_devolucion = fake.date_between(start_date=fecha_remate, end_date=datetime.date(2024, 12, 31)) if devolucion_garantia else None
    
    # Comportamiento web
    clicks_inicio = random.randint(0, 100)
    clicks_quienes_somos = random.randint(0, 50)
    clicks_contacto = random.randint(0, 50)
    clicks_remates_activos = random.randint(0, 200)
    clicks_abonar_garantia = random.randint(0, 50)
    clicks_agregar_al_carro = random.randint(0, 100)
    clicks_salon_remate = random.randint(0, 100)
    
    data.append([
        nombre, apellido, rut, direccion, comuna, cuenta_corriente, banco, monto_garantia, fecha_pago_garantia,
        n_jornada_remate, fecha_remate, modelo_auto, categoria_auto, proveedor_auto, pago_restante,
        fecha_pago_restante, devolucion_garantia, fecha_devolucion, clicks_inicio, clicks_quienes_somos,
        clicks_contacto, clicks_remates_activos, clicks_abonar_garantia, clicks_agregar_al_carro, clicks_salon_remate
    ])

# Crear DataFrame
columns = [
    'Nombre', 'Apellido', 'RUT', 'Dirección', 'Comuna', 'N° Cuenta Corriente', 'Banco', 'Monto de Garantía',
    'Fecha de Pago de Garantía', 'N° Jornada de Remate', 'Fecha del Remate', 'Modelo de Automóvil', 'Categoría de Automóvil',
    'Proveedor del Auto', 'Pago del Restante', 'Fecha de Pago del Restante', 'Devolución de Garantía', 'Fecha de Devolución',
    'Cantidad de Click en Inicio', 'Cantidad de Click en "Quiénes Somos"', 'Cantidad de Click en Contacto',
    'Cantidad de Click en Remates Activos', 'Cantidad de Click en Abonar Garantía', 'Cantidad de Click en Agregar al Carro',
    'Cantidad de Click a Salón de Remate'
]

df = pd.DataFrame(data, columns=columns)

# Guardar DataFrame en un archivo CSV
df.to_csv('mundo_ideal_karcal.csv', index=False)

print("Archivo CSV generado exitosamente.")
