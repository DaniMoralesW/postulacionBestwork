import pandas as pd

# Leer el archivo de Excel
df = pd.read_excel('PRUEBA PRACTICANTE.xlsx')

# Función para generar el usuario
def crear_usuario(fila):
    rut = fila['Rut']
    nombre = str(fila['Nombre']) #Tuve que convertirlo a string para poder separar
    nombre_split = nombre.split() #Separar el nombre
    nombre_primera_letra = nombre_split[0][0].upper()  # Selecciona la primera letra del nombre
    apellido_primera_letra = nombre_split[-1][0].upper()  # Selecciona la primera letra del apellido
    usuario = f"{rut}{nombre_primera_letra}{apellido_primera_letra}" #Definir el usuario según las instrucciones
    return usuario 

# Aplicar la función a cada fila del DataFrame
df['Usuario'] = df.apply(crear_usuario, axis=1)

# Mostrar el DataFrame con la nueva columna de usuarios
print(df[['Usuario']])