import os
import sys

# Ruta del archivo config.txt en el mismo directorio que el .exe
directorio_ejecucion = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
ruta_config = os.path.join(os.path.dirname(sys.executable), 'config.txt')
archivo_salida= os.path.join(directorio_ejecucion, 'ListadeArchivos.txt')

# Función para leer configuración en formato: clave valor
def leer_configuracion(ruta_config):
    configuracion = {}
    with open(ruta_config, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == '' or linea.startswith('#'):
                continue
            partes = linea.split(None, 1)  # separa por espacios o tabs
            if len(partes) == 2:
                clave, valor = partes
                configuracion[clave.strip().lower()] = valor.strip()  # <-- claves en minúsculas
    return configuracion

# Leer configuración desde el archivo
config = leer_configuracion('config.txt')

# Obtener las rutas desde las claves (en minúscula)
nombre_archivo = 'archivos.txt'
carpeta = config.get('carpeta')


# Validar que ambas rutas existan en la config
if not carpeta :
    print("❌ Error: Faltan las claves 'carpeta' ")
    exit(1)

# Verificar que la carpeta exista
if not os.path.isdir(carpeta):
    print(f"❌ Error: La carpeta '{carpeta}' no existe.")
    exit(1)

# Obtener la lista de archivos (no carpetas)
try:
    nombres_archivos = [
        f for f in os.listdir(carpeta)
        if os.path.isfile(os.path.join(carpeta, f))
    ]
except Exception as e:
    print(f"❌ Error al listar los archivos: {e}")
    exit(1)

# Escribir los nombres en el archivo de salida
try:
    with open(archivo_salida, 'w', encoding='utf-8') as salida:
        for nombre in nombres_archivos:
            salida.write(nombre + '\n')
    print(f"✅ Se guardaron {len(nombres_archivos)} nombres en: {archivo_salida}")
    os.startfile(archivo_salida)
except Exception as e:
    print(f"❌ Error al escribir el archivo de salida: {e}")
